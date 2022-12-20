from __future__ import print_function, unicode_literals
from facepplib import FacePP, exceptions
import emoji
from utils import script
import cv2, os


# define global variables
face_detection = ""
faceset_initialize = ""
face_search = ""
face_landmarks = ""
dense_facial_landmarks = ""
face_attributes = ""
beauty_score_and_emotion_recognition = ""


def linker(
    language,
    search_keyword,
    face_search=None,
    file_format=None,
    file=None,
    face_path=None,
):
    obj = script.ArchiveIdentifier(
        language=language,
        search_keyword=search_keyword,
        file_format=file_format,
        file=file,
        face_path=face_path,
    )
    print(obj)
    obj.run()

    obj.search_and_display()


def image_save(img):
    with open("utils/images_file.pdf_dir/input_image.jpg", "wb") as f:
        # Iterate over the chunks of the uploaded file
        # and write them to the destination file
        for chunk in img.chunks():
            f.write(chunk)
    return "utils/images_file.pdf_dir/input_image.jpg"


def face_save(img):
    with open("utils/input_face.jpg", "wb") as f:
        # Iterate over the chunks of the uploaded file
        # and write them to the destination file
        for chunk in img.chunks():
            f.write(chunk)
    return "utils/input_face.jpg"


# define face comparing function
def face_comparing(app, Image1, Image2):

    cmp_ = app.compare.get(image_file1=Image1, image_file2=Image2)

    print("Photo1", "=", cmp_.image1)
    print("Photo2", "=", cmp_.image2)

    # Comparing Photos
    print("Confidence = ", cmp_.confidence)
    if cmp_.confidence > 70:
        print("Both photographs are of same person......")
        return True
    else:
        print("Both photographs are of two different persons......")
        return False


def check(image1, image2):
    # api details
    api_key = "xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl"
    api_secret = "TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D"

    try:

        app_ = FacePP(api_key=api_key, api_secret=api_secret)
        funcs = [
            face_detection,
            faceset_initialize,
            face_search,
            face_landmarks,
            dense_facial_landmarks,
            face_attributes,
            beauty_score_and_emotion_recognition,
        ]

        # Pair 1
        # image1 = 'https://wikibio.in/wp-content/uploads/2017/11/Mouni-Roy-.jpg'
        # image2 = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Katrina_Kaif_promoting_Bharat_in_2019.jpg'
        return face_comparing(app_, image1, image2)

    except exceptions.BaseFacePPError as e:
        print("Error:", e)
        return False
