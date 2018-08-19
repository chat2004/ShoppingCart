from enum import Enum


class User(object):
    def __init__(self, name, email, group):
        self.name = name
        self.email = email
        self.group = group


class UserGroup(Enum):
    UNREGISTER = 'UNREGISTER'
    REGISTER = 'REGISTER'
    SILVER = 'SILVER'
    GOLD = 'GOLD'
