# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


from . import user
from . import quote
from . import quote_rating
