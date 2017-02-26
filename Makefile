.PHONY: run shell

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
