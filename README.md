# SOAP-REST-DJANGO

Example of MICROSERVICES using SOAP and REST app in django

SOAP microservice consist in a simple array sorter and REST resolves the common knapsack problem.

Installation tested on Ubuntu 20.04.1 LTS.

## Table of contents

- [Install pre-installation dependencies](#install-pre-installation-dependencies)
- [Create .env file](#create-env)
- [Start the server](#start-server)
- [References](#references)

### Install pre-installation dependencies <a name="install-pre-installation-dependencies"></a>

- Docker
  [Install](https://docs.docker.com/engine/install/ubuntu/)

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
