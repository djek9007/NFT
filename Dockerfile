FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /root/projects/var/www/nft/static/admin && \
    mkdir -p /root/projects/var/www/nft/media && \
    touch /root/projects/var/www/nft/static/admin/index.html

COPY . .

RUN python manage.py collectstatic --no-input

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 $WSGI_MODULE:application"]
