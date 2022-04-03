## ab_proxy_design
Proxy server design for A/B testing, written in Python with FastAPI.

### for local dev
```
❯ docker compose build
❯ docker compose up
```

or manually, 

```
❯ poetry install --no-root
❯ poetry run python mock/main.py
❯ poetry run python src/main.py
```

### for production use
Use [Dockerfile](./Dockerfile) to build and run with uvicorn.
