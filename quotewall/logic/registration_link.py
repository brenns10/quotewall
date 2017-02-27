# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta

from quotewall import db
from quotewall.models.registration_link import RegistrationLink
from quotewall.models.user import User
from quotewall.util.exc import UserException


def create_registration_link(uses=1, validity=timedelta(days=7)):
    link = RegistrationLink(uses, validity)
    db.session.add(link)
    db.session.commit()
    return link


def get_link_by_uuid(uuid):
    return RegistrationLink.query.filter(
        RegistrationLink.uuid == uuid
    ).one_or_none()


def delete_link_by_uuid(uuid):
    link = get_link_by_uuid(uuid)
    if link:
        db.session.delete(link)
        db.session.commit()
        return True
    else:
        return False


def register_user(uuid, username, email, password, real_name):
    # TODO: this is almost certainly not correct but it automatically updates
    link = get_link_by_uuid(uuid)
    if not link or datetime.now() > link.expires or link.uses <= 0:
        raise UserException('This registration link has expired.')
    user = User(username, email, password, real_name)
    user.registration_link = link
    link.uses = RegistrationLink.uses - 1
    db.session.add(link)
    db.session.add(user)
    db.session.commit()
    return user


def get_all_links():
    return RegistrationLink.query.all()
