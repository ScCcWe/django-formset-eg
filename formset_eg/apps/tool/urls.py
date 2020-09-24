# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: urls.py
# author: ScCcWe
# time: 2020/9/24 21:04


from django.urls import path

from . import views

app_name = 'tool'

urlpatterns = [
    path("", views.index, name="index-page"),
    path("update/<int:id>", views.update_tool_view, name="update-page"),
    path("create/", views.create_tool_view, name="create-page"),
]
