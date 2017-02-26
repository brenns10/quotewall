.PHONY: run shell

export FLASK_APP=quotewall
export FLASK_DEBUG=1
export QUOTEWALL_SETTINGS=$(shell pwd)/config_example.py

run: envvars
	flask run

shell: envvars
	flask shell --use-shell ptipython
