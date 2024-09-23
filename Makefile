.PHONY: run
run:
	python manage.py runserver

.PHONY: init
init: 
	pip install -r requirements.txt

.PHONY: css
css:
	npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch