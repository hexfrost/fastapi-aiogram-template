# FastAPI + Aiogram3 + UV 


* FastAPI
* Aiogram 3
* Uv
* Docker

## Quickstart

Copy example with required env variables
```bash
cp .env.example .env
```

Get `BOT_TOKEN` from [BotFather](https://t.me/botfather) and set it in `.env` file and set `BASE_DOMAIN` for webhook.


Your `.env` file should look like this:
```.env
BOT_TOKEN=6694236732:fvevftgvthjadafgvtvg 
BASE_DOMAIN=https://public-domain.example.com

APP_PORT=8000 # optional
APP_HOST=0.0.0.0 # optional

```

### Run with poetry

```bash
poetry install
```
   
### Run with docker-compose 
```bash
docker compose up --build

```

API will be available at `http://localhost:8000` by default.
