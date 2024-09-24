.PHONY: run
run:
	python manage.py runserver

.PHONY: init
init: 
	pip install -r requirements.txt

.PHONY: req
req:
	pip freeze > requirements.txt

.PHONY: css
css:
	npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch

.PHONY: migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate

.PHONY: super
super:
	python manage.py createsuperuser --email bercasiocharles14@gmail.com
