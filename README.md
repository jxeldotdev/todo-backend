
# todo-backend

"Todo list" Rest API written in python with user login support. See https://github.com/jxeldotdev/todo-frontend

## Usage

```shell
docker-compose up -d db
docker-compose pull
docker-compose run --rm app migrate
docker-compose up -d app
```

## Updating migrations
```shell
docker-compose run --rm --entrypoint sh app alembic revision --autogenerate -m "migration-name-here :)"
```

## Updating dependencies
Update requirements.txt to match pipenv by running the following:
```shell
pipenv run pip freeze > requirements.txt
```

## Contributing

Unfortunately for this repository pull requests will not be merged into this projcet as it is a personal showcase.


## Functionality / project checklist
- [x] Add logging to the application

- [x] Automate tests of App using CI



- [ ] Create a Helm chart for the application

- [ ] Create a seperate repo with Terraform configuration for EKS infrastructure

- [ ] Automate deployment of application

- [ ] Add monitoring to app with Prometheus
