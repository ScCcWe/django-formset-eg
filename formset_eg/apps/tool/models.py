from django.db import models

import datetime


class Tool(models.Model):
    name = models.CharField(verbose_name="工具名", max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '工具'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
