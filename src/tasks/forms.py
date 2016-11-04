from django import forms
from django_ace import AceWidget


class AceEditorForm(forms.Form):
    text = forms.CharField(widget=AceWidget(mode='css'))