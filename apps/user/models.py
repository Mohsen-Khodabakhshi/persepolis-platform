import re

from tortoise import fields
from tortoise.validators import RegexValidator

from helper.mixins.models import BaseModel

from apps.user.enums import UserType


class UserModel(BaseModel):
    EMAIL_VALIDATOR = RegexValidator(
        r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", re.I
    )

    first_name = fields.CharField(max_length=25)
    last_name = fields.CharField(max_length=25)
    username = fields.CharField(max_length=25, unique=True)
    email = fields.CharField(max_length=255, unique=True, validators=[EMAIL_VALIDATOR])
    active = fields.BooleanField(default=True)
    type = fields.CharEnumField(UserType, default=UserType.CLIENT)

    class Meta:
        table = "user"

    def __str__(self):
        return f"{self.username} - {self.type}"
