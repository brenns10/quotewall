# -*- coding: utf-8 -*-
import os.path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager

app = Flask('quotewall')
app.config.from_envvar('QUOTEWALL_SETTINGS')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'login_post'
login_manager.init_app(app)
migrate = Migrate(app, db, directory=os.path.join(__file__, 'migrations'))
manager = Manager(app)

import quotewall.views
import quotewall.models
import quotewall.scripts
