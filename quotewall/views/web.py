# -*- coding: utf-8 -*-
from quotewall import app


@app.route('/')
def hello():
    return 'hello'
