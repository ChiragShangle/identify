from django.shortcuts import render
from django.http import HttpResponse
from utils import helper

def identify_people(request):
    keyword = request.POST.get('keyword')
    file_type = request.POST.get('file_type')
    file_ = request.FILES.get('file')
    helper.image_save(file_)
    language = request.POST.get('language')
    face = request.FILES.get("face_search")
    print('hello')
    helper.linker(language=language, search_keyword = keyword, file_format = file_type, file=file_)
    return render(request,"index2.html")


def checking(request):
    return render(request,"index.html")
    