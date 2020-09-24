from django.db import models

import datetime

from apps.tool.models import Tool


class Version(models.Model):
    tool = models.ForeignKey(to=Tool, on_delete=models.CASCADE)
    version = models.CharField(verbose_name="工具版本", max_length=10)
    created = models.DateTimeField(default=datetime.datetime.now)
