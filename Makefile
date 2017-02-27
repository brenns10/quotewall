.PHONY: run shell migration migrate docker-first-run docker-update

export FLASK_APP=quotewall
export FLASK_DEBUG=1
export QUOTEWALL_SETTINGS=$(shell pwd)/config_example.py

run:
	flask run

shell:
	flask shell --use-shell ptipython

migration:
	cd quotewall; flask db migrate

migrate:
	cd quotewall; flask db upgrade

dist/quotewall-0.0.0-py3-none-any.whl: $(shell find quotewall -type f) setup.py
	python setup.py bdist_wheel

docker-first-run: dist/quotewall-0.0.0-py3-none-any.whl
	docker-compose up -d
	sleep 1
	docker-compose run web python3 -m quotewall init_db
	docker-compose run web python3 -m quotewall add_admin
	touch docker-build

docker-update: dist/quotewall-0.0.0-py3-none-any.whl
	docker-compose stop
	docker-compose up -d --build
	touch docker-build
