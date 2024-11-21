# Dockerfile

# Использование базового образа
FROM python:3.10-slim

# Установка зависимостей
RUN apt update && apt install -y \
    gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext vim

# Установка pip
RUN pip install --upgrade pip

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Копирование кода проекта
COPY . /app/

# Создание директорий для статики и медиа
RUN mkdir -p /app/static /app/media && \
    chmod -R 755 /app/static /app/media
