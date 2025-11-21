#!/bin/bash
set -e

PROJECT_DIR="/opt/Tur"
VENV_DIR="$PROJECT_DIR/venv"
GUNICORN_SERVICE="gunicorn_tur"
NGINX_SERVICE="nginx"

echo ">>> Переход в $PROJECT_DIR"
cd "$PROJECT_DIR"

echo ">>> Активирую виртуальное окружение"
source "$VENV_DIR/bin/activate"

echo ">>> Запускаю миграции"
python manage.py migrate --noinput

# Если нужно каждый раз собирать статику — раскомментируй следующие строки:
# echo ">>> Собираю статику"
# python manage.py collectstatic --noinput

echo ">>> Перезапускаю gunicorn ($GUNICORN_SERVICE)"
systemctl restart "$GUNICORN_SERVICE"

echo ">>> Перезапускаю nginx ($NGINX_SERVICE)"
systemctl restart "$NGINX_SERVICE"

echo ">>> Deploy завершён ✅"
