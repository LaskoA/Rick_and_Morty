# Rick and Morty
API service that scrapes data from official Rick and Morty API (https://rickandmortyapi.com/api/character).
There is a scheduled task, that checks API every minute and updates DB if new characters were created.
```shell
git clone https://github.com/LaskoA/Rick_and_Morty
cd Rick_and_MortyoodService

Virtual environment install for Windows:
  - python3 -m venv venv
  - venv\Scripts\activate
  
Virtual environment install for Mac:
  - sudo pip install virtualenv
  - virtualenv env
  - source env/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

Run Redis: docker run -d -p 6379:6379 redis

Run Celery Worker Windows: 
  celery -A rick_and_morty worker --loglevel=info -P eventlet
Run Celery Worker Mac: 
  celery -A rick_and_morty worker -l INFO

Run Celery Beat:
  celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

python manage.py runserver
```

## Description of endpoints
- http://127.0.0.1:8000/api/characters/ - shows list of all characters 
- http://127.0.0.1:8000/api/characters/random - shows information about 1 random character

## User for test
Login: admin
Password: admin12345