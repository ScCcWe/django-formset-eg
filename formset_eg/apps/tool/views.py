from django.shortcuts import render, redirect
from django import forms
from .forms import ToolForm
from .models import Tool

from apps.detail.forms import DetailForm
from apps.detail.models import Detail
from apps.version.models import Version
from apps.notice.models import Notice


def index(request):
    tools = Tool.objects.all()
    details = Detail.objects.all()
    notices = Notice.objects.all()
    versions = Version.objects.all()
    return render(request, 'tool/index.html', {
        "tools": tools,
        "details": details,
        "notices": notices,
        "versions": versions,
    })


def create_tool_view(request):
    notice_formset = forms.inlineformset_factory(Tool, Notice, fields=('notice',), extra=1)
    version_formset = forms.inlineformset_factory(Tool, Version, fields=('version',), extra=1)
    if request.method == 'POST':
        tool_form = ToolForm(request.POST)
        if tool_form.is_valid():
            new_tool = tool_form.save(commit=False)
            new_tool.save()
            # new_detail = DetailForm(request.POST)
            # if new_detail.is_valid():
            #     new_detail.save()
            notice_formset = notice_formset(request.POST, request.FILES, instance=new_tool)
            if notice_formset.is_valid():
                notice_formset.save()
            version_formset = version_formset(request.POST, request.FILES, instance=new_tool)
            if version_formset.is_valid():
                version_formset.save()
            return redirect("//127.0.0.1:8000/")
    else:
        tool_form = ToolForm()
        detail_form = DetailForm()
        notice_formset = notice_formset(queryset=Tool.objects.none())
        version_formset = version_formset(queryset=Tool.objects.none())
        return render(request, 'tool/create.html', {
            "tool_form": tool_form,
            # "detail_form": detail_form,
            'notice_formset': notice_formset,
            'version_formset': version_formset,
        })


def update_tool_view(request):
    if request.method == 'POST':
        ...
    else:
        ...
        return render(request, 'tool/update.html')
