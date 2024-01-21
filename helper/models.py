from tortoise import fields, Model


class TimeStampMixin:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class BaseModel(TimeStampMixin, Model):
    pass

    class Meta:
        abstract = True
