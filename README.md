# DenLeDa Тестовое задание
## Установка
```bash
git clone git@github.com:RG1ee/test-denleda.git
cd test-denleda

# Cкопируйте образец среды в `.env` и измените значения
cat env_sample > .env

# Собрать docker-compose с сервисом db
docker-compose up --build -d db
```

## Разработка
```bash
python3.11 -m venv .venv
. .venv/bin/activate

poetry install
pre-commit install
denleda migrate
```

## Запуск сервера
```bash
denleda runserver
```
## Запуск тестов
```bash
pytest
```
