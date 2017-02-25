# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import relationship
from sqlalchemy.sql import func

from models import Base


class QuoteRating(Base):
    __tablename__ = 'quote_ratings'

    quote_id = Column(Integer, ForeignKey('users.id'), primary_key=True,
                      nullable=False)
    quote = relationship('Quote', back_populates='ratings')
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True,
                     nullable=False)
    user = relationship('User', back_populates='ratings')

    rating = Column(Integer, nullable=False)
    time_created = Column(DateTime(timezone=True), nullable=False,
                          server_default=func.now())
