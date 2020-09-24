# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: forms.py
# author: ScCcWe
# time: 2020/9/24 20:57

from django import forms

from .models import Notice


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"
