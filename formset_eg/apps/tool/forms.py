# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: forms.py
# author: ScCcWe
# time: 2020/9/24 20:55

from django import forms

from .models import Tool


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ["name"]
