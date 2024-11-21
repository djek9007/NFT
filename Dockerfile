FROM docker.io/library/python:3.10-slim

# Использование bash
SHELL ["/bin/bash", "-c"]

# Настройки окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
USER nftuser
# Установка зависимостей
RUN apt update && apt install -y \
    gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext vim

# Установка pip
RUN pip install --upgrade pip

# Установка рабочего каталога
WORKDIR /root/projects/NFT
RUN chown -R nftuser:nftuser /root/projects/NFT
# Создание директорий для статики и медиа
RUN mkdir -p /root/projects/var/www/nft/static /root/projects/var/www/nft/media && \
    chmod -R 755 /root/projects/var/www/nft

# Копирование зависимостей
COPY requirements.txt /root/projects/NFT/
RUN pip install -r requirements.txt

# Копирование проекта
COPY . /root/projects/NFT/

# Пользователь для безопасности
RUN useradd -ms /bin/bash nftuser
RUN chown -R nftuser:nftuser /root/projects/NFT


# Запуск Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "my_project.wsgi:application"]
