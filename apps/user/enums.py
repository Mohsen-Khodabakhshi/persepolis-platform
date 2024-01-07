from enum import Enum


class UserType(str, Enum):
    ADMIN: str = "admin"
    CLIENT: str = "client"
