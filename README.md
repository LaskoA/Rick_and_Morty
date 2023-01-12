# Rick and Morty
API service that scrapes data from official Rick and Morty API (https://rickandmortyapi.com/api/character).
There is a scheduled task, that checks API every minute and updates DB if new characters were created.
```shell
git clone https://github.com/LaskoA/Rick_and_Morty
cd Rick_and_Morty

- create and fill .env file
- docker-compose up --build
```

## Description of endpoints
- http://127.0.0.1:8000/api/characters/ - shows list of all characters 
- http://127.0.0.1:8000/api/characters/random - shows information about 1 random character

## User for test
Login: admin
Password: admin12345