FROM python:3.10-slim

# Установка системных зависимостей
RUN apt update && apt install -y \
    gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext vim

# Обновление pip
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

# Открытие портов
EXPOSE 8000

# Команда запуска
CMD ["gunicorn", "my_project.wsgi:application", "--bind", "0.0.0.0:8000"]
