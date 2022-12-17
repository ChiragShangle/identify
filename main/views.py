from django.shortcuts import render
from django.http import HttpResponse
from utils import helper
import os

def identify_people(request):
    keyword = request.POST.get('keyword')
    file_type = request.POST.get('file_type')
    file_ = request.FILES.get('file')
    file_path =  helper.image_save(file_)
    language = request.POST.get('language')
    face = request.FILES.get("face_search")

    
    print(keyword, file_path)
    helper.linker(language=language, search_keyword = keyword, file_format = file_type, file=file_path)
    directory = 'utils/'
    file_names = os.listdir(directory)
    
    context = {
        'file_names': file_names,
    }

    return render(request, 'result.html', context)    



def checking(request):
    return render(request,"index.html")
    