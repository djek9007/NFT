# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /root/projects/nft

# Create directories for static and media files
RUN mkdir -p /root/projects/var/www/nft/media && \
    mkdir -p /root/projects/var/www/nft/static && \
    chmod -R 777 /root/projects/var/www/nft


# Copy dependency list
COPY ./requirements.txt ./requirements.txt

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the application port
EXPOSE 8000

# Default command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
