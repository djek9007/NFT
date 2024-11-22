# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Создаем родительскую папку и вложенные директории
RUN mkdir -p /root/var/www/nft/static /root/var/www/nft/media /root/var/www/nft/logs
RUN chmod -R 755 /root/var/www/nft

# Устанавливаем переменные окружения
ENV DJANGO_SETTINGS_MODULE=my_project.settings

# Запускаем сервер
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_project.wsgi:application"]
