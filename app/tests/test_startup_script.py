"""Never report another checkout's HTTP listener as our successful app start."""
import os
import shutil
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


def test_start_refuses_another_servers_port_without_spawning(tmp_path):
    root = Path(__file__).resolve().parents[2]
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    shutil.copyfile(root / "scripts/start.sh", scripts / "start.sh")
    bindir = tmp_path / "app/.venv/bin"
    bindir.mkdir(parents=True)
    (bindir / "python").symlink_to(sys.executable)

    class ForeignApp(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"another_app": true}')

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 0), ForeignApp)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        done = subprocess.run(["sh", str(scripts / "start.sh")],
                              env={**os.environ, "RAAG_PORT": str(server.server_port)},
                              capture_output=True, text=True, timeout=10)
        assert done.returncode != 0
        assert "already in use" in done.stderr
        assert "started (pid" not in done.stdout
        assert not (tmp_path / "data/server.pid").exists()
        assert not (tmp_path / "data/server.log").exists()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
