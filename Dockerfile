FROM python:3.10-slim

# Использование bash
SHELL ["/bin/bash", "-c"]

# Настройки окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создание пользователя для безопасности
RUN groupadd -g 1000 nftgroup || true && \
    useradd -ms /bin/bash -u 1000 -g nftgroup nftuser || true

# Установка зависимостей
RUN apt update && apt install -y \
    gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext vim && \
    pip install --upgrade pip

# Установка рабочего каталога
WORKDIR /root/projects/NFT

# Копирование зависимостей
COPY requirements.txt /root/projects/NFT/
RUN pip install -r requirements.txt

# Создание директорий для статики и медиа с правами
RUN mkdir -p /root/projects/var/www/nft/static /root/projects/var/www/nft/media && \
    chown -R nftuser:nftgroup /root/projects/var/www/nft/static /root/projects/var/www/nft/media && \
    chmod -R 775 /root/projects/var/www/nft/static /root/projects/var/www/nft/media

# Копирование проекта
COPY . /root/projects/NFT/

# Изменение владельца на пользователя nftuser
RUN chown -R nftuser:nftgroup /root/projects/NFT

# Переключение на пользователя nftuser для безопасности
USER nftuser

# Запуск Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "my_project.wsgi:application"]
