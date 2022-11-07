# SOAP-REST-DJANGO

Example of MICROSERVICES using SOAP and REST app in django

Installation tested on Ubuntu 20.04.1 LTS.

## Table of contents

- [Install pre-installation dependencies](#install-pre-installation-dependencies)
- [Create .env file](#create-env)
- [Setup dev enviroment](#setup-dev-env)
- [Create and activate virtual enviroment and install python dependencies](#setup-venv)
- [Setup de Database](#setup-db)
- [Start the server](#start-server)
- [Testing](#test)
- [References](#references)

## Steps by Virtual env <a name="virtualenv"></a>

This method is tested to work on linux, and is the most confortable for developing, because is faster in dev time, but need some pre working to start the enviroments

### Install pre-installation dependencies <a name="install-pre-installation-dependencies"></a>

- Docker
  Should come preinstalled with Ubuntu

### Create .env file <a name="create-env"></a>

On each microservice edit `.env.example` with your own settings and rename it `.env`
For the SECRET_KEY, one can generate it using `django shell`:

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

### Start the microserive <a name="start-server"></a>

Run the microservice on each folder

```bash
docker-compose up -d
```

## References <a name="references"></a>

- [Steps followed to setup django with postgreSQL][postgres]
- [Directory structure explanation](https://stackoverflow.com/questions/22841764/best-practice-for-django-project-working-directory-structure)

[postgres]: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
