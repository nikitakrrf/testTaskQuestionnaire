API-сервис для вопросов и ответов

Язык: Python 3.13
Фреймворк: Django 4.2 + Django REST Framework
База данных: PostgreSQL 16
Контейнеризация: Docker + Docker Compose v2


Установка Docker
https://docs.docker.com/engine/install/

Проверка
docker --version
docker compose version

Клонирование проекта
git clone https://github.com/nikitakrrf/testTaskQuestionnaire.git
cd testTaskQuestionnaire


Сборка образов
docker compose build --no-cache


Запуск контейнеров
docker compose up -d

Просмотр логов
docker compose logs -f

Открыть порт (По желанию)
sudo ufw allow 8000/tcp
