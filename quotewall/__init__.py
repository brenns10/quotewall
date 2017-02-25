# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_envvar('QUOTEWALL_SETTINGS')
db = SQLAlchemy(app)

import quotewall.views
import quotewall.models
