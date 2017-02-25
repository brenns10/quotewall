# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_envvar('QUOTEWALL_SETTINGS')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

import quotewall.views
import quotewall.models
