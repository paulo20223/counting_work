WEB_CONTAINER_NAME=work-web
WEB_SERVICE_NAME=web
DEFAULT_DB=postgres


cs: ## make collect static
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py collectstatic

cdD:
	python manage.py collectstatic

mkm: ## make migrations
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py makemigrations

m: ## migrate
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py migrate

csu: ## create superuser
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py createsuperuser

bash:
	docker exec -it ${WEB_CONTAINER_NAME} bash

rm_m:
	docker exec -it ${WEB_CONTAINER_NAME} find /code/apps/ -path "*/migrations/*" -not -name "__init__.py" -delete
	docker exec -it ${WEB_CONTAINER_NAME} find /code/core/ -path "*/migrations/*" -not -name "__init__.py" -delete
	docker exec -it ${WEB_CONTAINER_NAME} find /code/api/v1/ -path "*/migrations/*" -not -name "__init__.py" -delete

rn: ## Rebuild container, recreate migration, create superuser.
	docker-compose down
	docker-compose build
	docker-compose up -d web
	make rm_m
	make mkm
	make m
	make csu
	docker-compose stop

update: ## git pull and back web restart
	git pull
	docker-compose restart web

serve: ## run front server
	cd front && npm run serve

build: ## Build front and collect static
	cd front && npm run build
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py collectstatic


h: ## This help dialog.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

test:
	docker exec -it ${WEB_CONTAINER_NAME} ./manage.py test
