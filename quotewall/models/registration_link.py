# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import uuid

from quotewall import db


class RegistrationLink(db.Model):
    __tablename__ = 'registration_link'

    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)
    uuid = db.Column(db.String(32))
    uses = db.Column(db.Integer, default=1)
    expires = db.Column(db.DateTime(timezone=True), nullable=False)

    users = db.relationship('User', back_populates='registration_link')

    def __init__(self, uses=1, validity=timedelta(days=7)):
        self.uses = uses
        self.expires = datetime.now() + validity
        self.uuid = uuid.uuid4().hex
