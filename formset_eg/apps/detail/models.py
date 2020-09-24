from django.db import models

from apps.tool.models import Tool


class Detail(models.Model):
    tool = models.OneToOneField(to=Tool, on_delete=models.CASCADE)
    desc = models.TextField()
