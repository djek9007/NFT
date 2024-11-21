FROM python:3.10-slim

# Use bash for the shell
SHELL ["/bin/bash", "-c"]

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a user for security
RUN useradd -ms /bin/bash nftuser

# Install dependencies
RUN apt update && apt install -y \
    gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext vim

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /root/projects/NFT

# Copy the dependencies file first and install the dependencies
COPY requirements.txt /root/projects/NFT/
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . /root/projects/NFT/

# Change ownership of the project files to nftuser
RUN chown -R nftuser:nftuser /root/projects/NFT

# Create static and media directories
RUN mkdir -p /root/projects/var/www/nft/static /root/projects/var/www/nft/media && \
    chmod -R 755 /root/projects/var/www/nft

# Switch to the created user
USER nftuser

# Run migrations, collectstatic, and start Gunicorn
CMD ["bash", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn -b 0.0.0.0:8000 my_project.wsgi:application"]
