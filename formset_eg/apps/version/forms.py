# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: forms.py
# author: ScCcWe
# time: 2020/9/24 20:58


from django import forms

from .models import Version


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ["version"]


