FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=NFT.settings
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "NFT.wsgi:application"]
