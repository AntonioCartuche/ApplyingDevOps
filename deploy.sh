#!/bin/bash
echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Ejecutando migraciones..."
python manage.py migrate

echo "Corriendo pruebas..."
python manage.py test