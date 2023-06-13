# Mera

Сервис загружающий курсы валют из API Deribit

## Пререквизиты

Docker

## Стек

python 3.10

pytest-asyncio

PostgreSQL

alembic

pydantic

apscheduler

uvicorn

## Запуск

git clone git@github.com:Konstantin8891/Mera.git

cd Mera

nano .env

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

POSTGRES_DB=postgres

HOST=localhost

PORT=5440

uvicorn main:app --reload
