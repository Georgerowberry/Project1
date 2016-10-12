from django.shortcuts import render
from .forms import FileForm, MinuetsForm
from .models import File, Minuets


def UploadPage(request):
    return render(request, 'upload/upload_page.html'),


def SaveFile(request):
    saved = False

    if request.method == "POST":
        MyFileForm= FileForm(request.POST, request.FILES)

    if MyFileForm.is_valid():
        file = File()
        file.title = MyFileForm.cleaned_data["title"]
        file.save()
        saved = True

    else :
        MyFileForm = FileForm()

    return render(request, 'saved.html', locals())


def SaveMinuets(request):
    saved = False

    if request.method == "POST":
        MyMinuetsForm = MinuetsForm(request.POST, request.FILES)

    if MyMinuetsForm.is_valid():
        minuets = File()
        minuets.title = MyMinuetsForm.cleaned_data["title"]
        minuets.date = MyMinuetsForm.cleaned_data[""]
        minuets.save()
        saved = True

    else:
        MyMinuetsForm = MinuetsForm()

    return render(request, 'saved.html', locals())