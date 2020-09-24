from django.db import models

import datetime

from apps.tool.models import Tool


class Notice(models.Model):
    tool = models.ForeignKey(to=Tool, on_delete=models.CASCADE)
    notice = models.CharField(verbose_name="工具公告", max_length=50)
    created = models.DateTimeField(default=datetime.datetime.now)
