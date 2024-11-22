FROM python:3.10-slim

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y gcc libpq-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Создаём папки для статики и медиа
RUN mkdir -p /app/static /app/media

# Команда по умолчанию
CMD ["gunicorn", "my_project.wsgi:application", "--bind", "0.0.0.0:8000"]
