## Running on a local machine
```sh
cp example.env .env
docker-compose up -d --build
```

## Running tests
```sh
docker exec -it django_backend pytest
```