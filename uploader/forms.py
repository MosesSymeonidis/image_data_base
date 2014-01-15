# -*- coding: utf-8 -*-
from django import forms

class UploadFileForm(forms.Form):
        file  = forms.ImageField(label='Select a file')

class QueryFileForm(forms.Form):
        text = forms.TextInput()
        file  = forms.ImageField(label='Select a file')