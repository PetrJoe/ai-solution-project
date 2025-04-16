#!/bin/bash
set -e

# Update pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, uncomment if needed)
# python manage.py createsuperuser --noinput

# Set proper permissions
chmod -R 755 .

# Set environment variables for production
export DEBUG=False
export ALLOWED_HOSTS=".example.com,localhost,127.0.0.1"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file with secure secret key"
    python -c "import secrets; print('SECRET_KEY=' + secrets.token_urlsafe(50))" > .env
    echo "DEBUG=False" >> .env
    echo "ALLOWED_HOSTS=.example.com,localhost,127.0.0.1" >> .env
fi

echo "Build completed successfully!"
