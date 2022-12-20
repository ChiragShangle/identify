from django.shortcuts import render
from django.http import HttpResponse
from utils import helper
import os, shutil


def identify_people(request):
    try:
        keyword = request.POST.get("keyword")
        file_type = request.POST.get("file_type")
        file_ = request.FILES.get("file")
        file_path = helper.image_save(file_)
        language = request.POST.get("language")
        face = request.FILES.get("face")

        face_path = ""
        if face:
            face_path = helper.face_save(face)

        print("-----------Language----------======", language)
        helper.linker(
            language=language,
            search_keyword=keyword,
            file_format=file_type,
            file=file_path,
            face_path=face_path,
        )
    except Exception as e:
        print(e)
    finally:
        directory = "utils/results/"
        file_names = os.listdir(directory)

        context = {
            "file_names": file_names,
        }
        return render(request, "result.html", context)


def checking(request):
    if os.path.exists("utils/results"):
        shutil.rmtree("utils/results")
        os.mkdir("utils/results")
    return render(request, "index.html")
