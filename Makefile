.PHONY: run-dev

run-dev:
	FLASK_APP=quotewall/__init__.py \
	FLASK_DEBUG=1 \
	QUOTEWALL_SETTINGS=$(shell pwd)/config_example.py \
	flask run

shell-dev:
	FLASK_APP=quotewall/__init__.py \
	FLASK_DEBUG=1 \
	QUOTEWALL_SETTINGS=$(shell pwd)/config_example.py \
	flask shell
