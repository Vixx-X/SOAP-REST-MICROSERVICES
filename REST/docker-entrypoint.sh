set -e

if [ "$1" = 'rest' ]; then
	# Apply database migrations
	echo "Apply database makemigrations"
	python manage.py makemigrations

	echo "Apply database migrations"
	python manage.py migrate

	# python manage.py createsuperuser --username admin --email admin@dev.com
	echo "from django.contrib.auth.models import User; users=User.objects; users.filter(username='admin').exists() or users.create_superuser('admin','admin@dev.com','abcd1234$')" | python manage.py shell

	# Start server
	echo "Starting server"
	python manage.py runserver 0.0.0.0:8000
fi

exec "$@"

