from django.shortcuts import render
from django.http import HttpResponse
from utils import helper

def search_view(request):
    keyword = request.POST.get('keyword')
    file_type = request.POST.get('file_type')
    file_ = request.FILES.get('file')
    language = request.POST.get('language')
    face = request.FILES.get("face_search")


    return HttpResponse('Success')


def checking(request):
    return render(request,"index.html")