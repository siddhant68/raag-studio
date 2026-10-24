# Credits and licensing

Raag Studio's application code and documentation are licensed under the MIT license in LICENSE.
It was created by Siddhant Pathak. The clean application release is derived from the working
Raag Studio development snapshot `611bb52198eb817c1a56b5586ff6acdb65c8c1db`.

Music generation is powered by [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5),
developed by the ACE-Step team. The tested source is pinned to
`ca1e85fe9430179831e6bc6be790c332190a3866`. Its
[license](https://github.com/ace-step/ACE-Step-1.5/blob/ca1e85fe9430179831e6bc6be790c332190a3866/LICENSE)
and dependencies remain separate; no engine source or weights are redistributed here.

The optional engine installer retrieves the turbo DiT, VAE and Qwen embedding from the
[ACE-Step model repository](https://huggingface.co/ACE-Step/Ace-Step1.5), pinned to
`19671f406d603126926c1b7e2adc169acbcade22`. Check upstream model cards and notices for the
specific artifacts you use. The Qwen embedding model is distinct from the optional 5Hz music LM.

FastAPI, Starlette, Pydantic, Uvicorn, HTTPX, PyTorch, MLX and FFmpeg are independent projects,
used under their respective licenses. They are installed separately rather than vendored.
FFmpeg builds may have different licensing terms depending on enabled codecs.

Optional Claude planning uses Anthropic's services under the user's own account and terms.
Raag Studio is not affiliated with or endorsed by Anthropic or the ACE-Step team.

The showcase contains AI-generated example performances and original lyric sheets supplied for
evaluation. The software license does not promise copyright ownership, exclusivity, commercial
clearance or third-party rights in generated output. Use inputs you have permission to use.
