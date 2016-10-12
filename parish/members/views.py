from django.http import Http404
from .models import Member
from django.shortcuts import render


def index(request):
    all_members = Member.objects.all()
    return render(request, 'members/index.html', {'all_members': all_members})


def detail(request, member_id):
    try:
        member = Member.objects.get(pk=member_id)
    except Member.DoesNotExist:
        raise Http404("Member Does not Exist")
    return render(request, 'members/detail.html', {'member': member})

