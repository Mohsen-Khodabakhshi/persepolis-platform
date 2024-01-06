import re

from tortoise import fields
from tortoise.validators import RegexValidator

from helper.mixins.models import BaseModel


class UserModel(BaseModel):
    ADMIN = 10
    CLIENT = 20
    USER_TYPES = (
        (ADMIN, "Admin"),
        (CLIENT, "Client"),
    )

    EMAIL_VALIDATOR = RegexValidator(
        r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", re.I
    )

    first_name = fields.CharField(max_length=25)
    last_name = fields.CharField(max_length=25)
    username = fields.CharField(max_length=25, unique=True)
    email = fields.CharField(max_length=255, unique=True, validators=[EMAIL_VALIDATOR])
    active = fields.BooleanField(default=True)
    type = fields.SmallIntField(choices=USER_TYPES, default=CLIENT)

    class Meta:
        table = "user"

    def __str__(self):
        return f"{self.username} - {self.type}"
