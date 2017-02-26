# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('quotewall')
app.config.from_envvar('QUOTEWALL_SETTINGS')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'login_post'
login_manager.init_app(app)
migrate = Migrate(app, db)

import quotewall.views
import quotewall.models
