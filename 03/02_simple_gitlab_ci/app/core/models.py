from django.db import models
from django.db.models import TextField


class EmpireAgent(models.Model):
    first_name = TextField(null=True)
    last_name = TextField(null=True)
    email = TextField(null=True)
