# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Создаем директории для статических и медиа файлов и устанавливаем права доступа
RUN mkdir -p /app/static /app/media
RUN chmod -R 755 /app/static /app/media

# Устанавливаем переменные окружения
ENV DJANGO_SETTINGS_MODULE=my_project.settings

# Запускаем сервер
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_project.wsgi:application"]
