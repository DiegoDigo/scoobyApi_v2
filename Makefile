runserver-local:
	python manage.py runserver

runserver-externo:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

test:
	python manage.py test tests.models

shell:
	python manage.py shell
