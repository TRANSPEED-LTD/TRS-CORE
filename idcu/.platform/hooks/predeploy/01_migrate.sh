#!/bin/bash
# Navigate to the application directory
cd /var/app/current

# Activate the virtual environment (if necessary)
if [ -d "/var/app/venv" ]; then
    source /var/app/venv/*/bin/activate
fi

# Run migrations
python manage.py migrate --noinput

# Run collect static
python manage.py collectstatic --noinput