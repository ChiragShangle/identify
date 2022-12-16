from utils import script
import cv2 , os
def linker(language, search_keyword, face_search=None, file_format=None, file=None):
    if face_search==None:
    
        obj = script.ArchiveIdentifier(language=language, search_keyword = search_keyword, file_format = file_format, file=file)
        print(obj)
        obj.run()
       
        obj.search_and_display()
        
def image_save(img):
    
    with open('utils/images_file.pdf_dir/input_image.jpg', 'wb') as f:
        # Iterate over the chunks of the uploaded file
        # and write them to the destination file
        for chunk in img.chunks():
            f.write(chunk)
    return 'utils/images_file.pdf_dir/input_image.jpg'

