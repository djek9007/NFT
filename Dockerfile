FROM python:3.10-slim

WORKDIR /root/projects/NFT

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /root/projects/var/www/nft/static /root/projects/var/www/nft/media /root/projects/var/www/nft/logs
RUN chmod -R 777 /root/projects/var/www/nft/static /root/projects/var/www/nft/media /root/projects/var/www/nft/logs

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_project.wsgi:application"]
