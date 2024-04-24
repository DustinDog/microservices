#!/bin/sh

echo "Running Database Migrations"
python account_service/manage.py makemigrations
python account_service/manage.py migrate
echo "Running Database Migrations successful"

exec "$@"
