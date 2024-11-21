# Используем Python 3.10 Slim
FROM python:3.10-slim

# Устанавливаем зависимости
RUN apt update && apt install -y \
    gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext vim

# Устанавливаем pip
RUN pip install --upgrade pip

# Настроим рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Ожидаем прав на директории
RUN mkdir -p /app/static /app/media && \
    chmod -R 755 /app/static /app/media

# Запуск Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "my_project.wsgi:application"]
