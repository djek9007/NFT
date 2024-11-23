FROM python:3.6

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Создаем директории для статики, медиа и логов, и задаем разрешения
RUN mkdir -p /app/staticfiles /app/media /root/var/www/nft/media /root/var/www/nft/logs && \
    chmod -R 755 /app/staticfiles /app/media /root/var/www/nft/media /root/var/www/nft/logs

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Открываем порт для приложения
EXPOSE 8000

# Запускаем сервер
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn acmo.wsgi:application --bind 0.0.0.0:8000"]
