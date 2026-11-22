# drf_template

<!-- toc -->

- [local deployment](#local-deployment)
  - [requirements](#requirements)

<!-- tocstop -->

this is an API developed using drf,

## local deployment

### requirements

- docker
- Docker compose
- a text editor

```bash
$ docker compose build
$ docker compose up
# run the migrations
$ docker compose run api  python manage.py migrate
# optional you can fill with dummy data using
$ docker compose run api python manage.py seed [app] --number=[int] # replace [app] whit area, expertise, user, mentor, avaliability and [int] with any number
```

now you can read the schema declaration in the `http://localhost:8000/swagger/` address

to authenticate first you need to create a super user with django

```bash
docker compose run api python manage.py createsuperuser
```

and fill the data

## Repository reference

| Path                                         | Purpose                                  |
| -------------------------------------------- | ---------------------------------------- |
| [`drf_api/`](drf_api/)                       | Django project settings                  |
| [`users/`](users/)                           | Shared user or application configuration |
| [`docker-compose.yaml`](docker-compose.yaml) | Compose services                         |
| [`requirements.txt`](requirements.txt)       | Python dependencies                      |

The default branch is `main`. Use the tracked manifests and scripts above
when preparing changes; keep local credentials and generated files out of commits.
