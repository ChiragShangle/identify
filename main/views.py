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
    # files = []
    # for x in file_names:
    #     x = "{% static \'assets\img\x5c" + x + "\'%}"
    #     files.append(x)
    # print(files)   
    # Pass the array of file names to the template context
    context = {
        'file_names': file_names,
    }

    return render(request, 'index3.html', context)    



def checking(request):
    return render(request,"index.html")
    
def test(request):
    return render(request,"index2.html")
    