CUSTOM_USER_PATCH=/code/back/apps/user/migrations/0001_initial.py

h: ## help dialog
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

b: ## Build
	docker-compose build

bP: ## Build
	docker-compose -f docker-compose.production.yml build

bn: ## Build no cache
	docker-compose build --no-cache

mkm:  ## Make migrations
	docker-compose exec web python manage.py makemigrations

mkmP:  ## Make migrations
	docker-compose -f docker-compose.production.yml exec web python manage.py makemigrations

m:  ## Make migrate
	docker-compose exec web python manage.py migrate

mP:
	docker-compose -f docker-compose.production.yml exec web python manage.py migrate

cs: ## Collect static
	docker-compose exec web python manage.py collectstatic --noinput

csP:
	docker-compose -f docker-compose.production.yml exec web python manage.py collectstatic --noinput

csu: ## Create super user
	docker-compose exec web python manage.py createsuperuser

csuP: ## Create super user
	docker-compose -f docker-compose.production.yml exec web python manage.py createsuperuser


sh: ## Django shell
	docker-compose exec web python manage.py shell

bash: ## Bash container
	docker-compose exec web bash

up: ## Up all containers
	docker-compose up -d

upP: ## Up all containers
	docker-compose -f docker-compose.production.yml up -d


i: s mkm m cs

l: ## Open logs
	docker-compose logs -f

r: ## Restart
	docker-compose restart

rP:
	docker-compose -f docker-compose.production.yml restart

s: ## Start
	docker-compose up -d postgres
	docker-compose up -d web

stop: ## Stop
	docker-compose stop

d: ## Down with volumes
	docker-compose down --volumes

dP:
	docker-compose -f docker-compose.production.yml down --volumes

update: ## git pull and back web restart
	git pull
	make mkm
	make m
	docker-compose restart web

rm_m: ## Remove migrations
	docker-compose exec web find /code/back/apps/ -path "*/migrations/*" -not -name "__init__.py" -not -wholename "${CUSTOM_USER_PATCH}" -delete
	docker-compose exec web find /code/back/core/ -path "*/migrations/*" -not -name "__init__.py" -delete
	docker-compose exec web find /code/back/api/v1/ -path "*/migrations/*" -not -name "__init__.py" -delete

rm_mP:
	docker-compose -f docker-compose.production.yml exec web find /code/back/apps/ -path "*/migrations/*" -not -name "__init__.py" -not -wholename "${CUSTOM_USER_PATCH}" -delete
	docker-compose -f docker-compose.production.yml exec web find /code/back/core/ -path "*/migrations/*" -not -name "__init__.py" -delete
	docker-compose -f docker-compose.production.yml exec web find /code/back/api/v1/ -path "*/migrations/*" -not -name "__init__.py" -delete

rn: ## Recreate all
	make d
	make b
	make up
	make m
	make mkm
	make m
#	make csu
	make fake
	docker-compose stop

rnP: ## Recreate all
	make dP
	make bP
	make upP
	make mP
	make mkmP
	make mP
#	make csuP
	make fakeP
	docker-compose -f docker-compose.production.yml stop

serve: ## Run front dev server
	cd front && npm run dev

build: ## Build front and collect static
	cd front && npm run generate
	make cs

fake:
	docker-compose exec web python manage.py fake

fakeP: ## set fake data
	docker-compose -f docker-compose.production.yml exec web python manage.py fake

flush: ## clear all data
	docker-compose exec web python manage.py flush --noinput
	docker-compose exec web find media/ -path "*" -delete

flushP: ## clear all prod data
	docker-compose -f docker-compose.production.yml exec web python manage.py flush --noinput

shell:
	docker-compose  exec web python manage.py shell

