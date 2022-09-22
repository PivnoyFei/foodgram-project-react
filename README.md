<h1 align="center"><a target="_blank" href="https://github.com/PivnoyFei/praktikum_new_diplom/">Проект Продуктовый помошник</a></h1>
![Foodgram workflow](https://github.com/PivnoyFei/praktikum_new_diplom/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание
Проект Foodgram, «Продуктовый помощник». На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Стек:
```bash Python 3.7, Django 2.2.19, Django REST Framework, PostgreSQL 13.0, Docker, Docker Hub, Nginx, Gunicorn 20.0.4, GitHub Actions, Yandex.Cloud.```

### Шаблон создания файла .env расположенный по пути infra/.env
```bash
DB_ENGINE=django.db.backends.postgresql  # движок БД
DB_NAME=postgres  # имя БД
POSTGRES_USER=postgres  # логин для подключения к БД
POSTGRES_PASSWORD=postgres  # пароль для подключения к БД
DB_HOST=db  # название контейнера
DB_PORT=5432  # порт для подключения к БД
ALLOWED_HOSTS=*
SECRET_KEY=key  # секретный ключ Django
```

### Для работы с Workflow в репозитории на Гитхабе добавьте данные в ```Settings - Secrets - Actions secrets```:
```
DOCKER_USERNAME - имя пользователя в DockerHub
DOCKER_PASSWORD - пароль пользователя в DockerHub

HOST - публичный ip-адрес сервера
USER - пользователь
SSH_KEY - приватный ssh-ключ (публичный должен быть на сервере)
PASSPHRASE - если используете пароль для ssh

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS - Ваш хост
SECRET_KEY=key - секретный ключ приложения django

TELEGRAM_TO - id своего телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
TELEGRAM_TOKEN - токен бота (получить токен можно у @BotFather, /token, имя бота)
```

### Запуск проекта:
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/PivnoyFei/praktikum_new_diplom
cd praktikum_new_diplom
```

Создаем и активируем виртуальное окружение для linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```

Обновиляем pip:
```bash
python -m pip install --upgrade pip
```

Обновиляем pip и установим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip &&
pip install -r backend/requirements.txt
```

Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```

Запуск docker-compose:
```bash
docker-compose up -d --build
```

После успешной сборки на сервере выполните команды (только после первого деплоя):
Соберите статические файлы:
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

Примените миграции:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput
```

Загрузите ингридиенты в базу данных:
в папке data - ingredients.json, tags.json
```bash
docker-compose exec backend python manage.py load_ingredients <Название файла>
```

Теперь проект доступен по адресу http://localhost/,  
документация по API проекта - по адресу http://localhost/api/docs/.


Создайте суперпользователя Django:
```bash
docker-compose exec backend python manage.py createsuperuser
```

Теперь по адресу http://localhost/admin/ доступна админка.

Останавливаем контейнеры:
```bash
docker-compose down -v
```

### Разработчики проекта
[Смелов Илья](https://github.com/PivnoyFei)
