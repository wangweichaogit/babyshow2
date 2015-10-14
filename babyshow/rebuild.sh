#! /bin/sh 

python manage.py migrate
python manage.py makemigretions
python manage.py migrate

python test.py
