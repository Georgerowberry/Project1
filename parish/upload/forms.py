from django import forms


class FileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()


class MinuetsForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()
    date = forms.DateField()
