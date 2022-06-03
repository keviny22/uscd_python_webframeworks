import uuid

from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)