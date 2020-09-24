# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: forms.py
# author: ScCcWe
# time: 2020/9/24 20:59


from django import forms

from .models import Detail


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ["desc"]
