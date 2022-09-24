<h1 align="center"><a target="_blank" href="https://github.com/PivnoyFei/foodgram-project-react/">Проект Продуктовый помошник</a></h1>

![Foodgram workflow](https://github.com/PivnoyFei/foodgram-project-react/actions/workflows/main.yml/badge.svg)

#### Проект запущен по адресу http://84.201.140.26/

#### Данные для входа с правами администратора:
```
email = admin@fake.fake
password = admin_fake
```

## Описание
Проект Foodgram, «Продуктовый помощник». На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Стек:
```bash Python 3.7, Django 2.2, Django REST Framework, PostgreSQL 13.0, Docker, Docker Hub, Nginx, Gunicorn 20.0.4, GitHub Actions, Yandex.Cloud.```

### Для работы с Workflow в репозитории на Гитхабе добавьте данные в ```Settings - Secrets - Actions secrets```:
```
DOCKER_USERNAME = имя пользователя в DockerHub
DOCKER_PASSWORD = пароль пользователя в DockerHub

HOST = публичный ip-адрес сервера
USER = пользователь для подключения к серверу
SSH_KEY = приватный ssh-ключ (публичный должен быть на сервере)
PASSPHRASE = если используете пароль для ssh

TELEGRAM_TO = id своего телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
TELEGRAM_TOKEN = токен бота (получить токен можно у @BotFather, /token, имя бота)

Следующие переменные также нужно добавить в файлй .env расположенный по пути infra/.env

DB_ENGINE=django.db.backends.postgresql  # движок БД
DB_NAME=postgres  # имя БД
POSTGRES_USER=postgres  # логин для подключения к БД
POSTGRES_PASSWORD=postgres  # пароль для подключения к БД
DB_HOST=db  # название контейнера
DB_PORT=5432  # порт для подключения к БД
ALLOWED_HOSTS=*, localhost # указываем разрешенные хосты
SECRET_KEY=key # секретный ключ приложения django
```

## Запуск проекта:
#### Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/PivnoyFei/foodgram-project-react
cd foodgram-project-react
```

#### Создаем и активируем виртуальное окружение для linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```

#### Обновиляем pip и установим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip &&
pip install -r backend/requirements.txt
```

#### Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```

#### Запуск docker-compose:
```bash
docker-compose up -d --build
```

#### После успешной сборки на сервере выполните команды (только после первого деплоя):
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

#### Примените миграции:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput
```

#### Команда для заполнения базы начальными данными (необязательно):
```bash
docker-compose exec backend python manage.py loaddata db.json
```

#### Загрузите подготовленные ингридиенты и теги в базу данных:
в папке data - ```ingredients.json, tags.json```
```bash
docker-compose exec backend python manage.py load_ingredients <Название файла>
```

Теперь проект доступен по адресу http://localhost/,  
документация по API проекта - по адресу http://localhost/api/docs/.


#### Создайте суперпользователя Django:
```bash
docker-compose exec backend python manage.py createsuperuser
```

Теперь по адресу http://localhost/admin/ доступна админка.

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```

## Как запустить проект на сервере:
### Подключиться к серверу из терминала
```bash
ssh <username>@<ip-adress>
```

#### Установите Docker и Docker-compose:
```bash
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
#### Проверьте корректность установки Docker-compose:
```bash
sudo docker-compose --version
```

### Зайдите в репозиторий в котором расположены файлы на локальной машине и отправьте файлы на сервер.

#### Отредактируйте файл ```nginx.conf``` и в строке ```server_name``` впишите публичный ip сервера.
#### Скопируйте файлы ```docker-compose.yaml``` и ```nginx.conf``` из вашего проекта на сервер:
```bash
sudo mkdir <создает нужную папка>
scp docker-compose.yaml <username>@<host>:<Нужная папка>/docker-compose.yaml
scp default.conf <username>@<host>:<Нужная папка>/nginx.conf
```
#### или чтобы скопировать каталог infra, активируйте флаг -r
```bash
scp -r infra <username>@<host>:/infra
```

### Разработчики проекта
[Смелов Илья](https://github.com/PivnoyFei)
