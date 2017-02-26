.PHONY: run-dev

run:
	FLASK_APP=quotewall \
	FLASK_DEBUG=1 \
	QUOTEWALL_SETTINGS=$(shell pwd)/config_example.py \
	flask run

shell:
	FLASK_APP=quotewall \
	FLASK_DEBUG=1 \
	QUOTEWALL_SETTINGS=$(shell pwd)/config_example.py \
	flask shell --use-shell ptipython
