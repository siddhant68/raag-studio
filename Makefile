PYTHON := app/.venv/bin/python

.PHONY: setup start stop doctor test test-ui
setup:
	./scripts/setup.sh
start:
	./scripts/start.sh
stop:
	./scripts/stop.sh
doctor:
	$(PYTHON) scripts/preflight.py --json
test:
	$(PYTHON) -m pytest -q
test-ui:
	node --test app/tests/js/logic.test.mjs
