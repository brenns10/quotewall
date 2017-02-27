# -*- coding: utf-8 -*-


class UserException(Exception):

    def __init__(self, user_message, is_error=True):
        self.user_message = user_message
        self.is_error = is_error
