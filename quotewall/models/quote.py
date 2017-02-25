# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import relationship
from sqlalchemy.sql import func

from models import Base


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    poster_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    poster = relationship("User", back_populates='posts',
                          foreign_keys=['poster_id'])
    quoted_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    quoted = relationship('User', back_populates='quotes',
                          foreign_keys=['quoted_id'])
    text = Column(Text, nullable=False)

    time_created = Column(DateTime(timezone=True), nullable=False,
                          server_default=func.now())

    rating_count = Column(Integer, nullable=False, default=0)
    rating_sum = Column(Integer, nullable=False, default=0)

    ratings = relationship('QuoteRating', back_populates='quote')
