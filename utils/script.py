import zipfile
from zipfile import ZipFile
import PIL
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
import shutil
import uuid
from pdf2image import convert_from_path


class ArchiveIdentifier:
    def __init__(
        self, language, search_keyword, face_search=None, file_format=None, file=None
    ):
        self.language = language  # Language (Hindi / English)
        self.search_keyword = search_keyword  # Any Identity Name
        self.face_search = face_search  # Face search if photo is provided
        self.file_format = file_format  # File format (pdf/ jpg/ zip/ png)
        self.file = file  # Original file

        self.images_file_dir = 'images_file.pdf_dir'
        # pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
        
        pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR"
        self.face_cascade = cv.CascadeClassifier(r"utils/haarcascade.xml")


        '''
        If given file is jpg or pdf.. converting it into zip file ("zip_file.zip")
        '''
        if self.file_format=='pdf':
            self.convert_pdf_to_images()
            self.convert_image_into_zip()
            self.file = r"utils/zip_file.zip"

        if self.file_format=='image':
            self.convert_image_into_zip()
            self.file = r"utils/zip_file.zip"

        '''
        Convert into zip first
        '''
        self.zip_file = zipfile.ZipFile(self.file)
        self.inflist = self.zip_file.infolist()

        self.image_array = []

        self.image_dic = dict()
        self.text_dic = dict()

    def collage_maker(self):
        """
        Function to make the collage of all the image
        """
        if len(self.image_array) == 0:
            return None
        first_image = self.image_array[0]
        images_count = len(self.image_array)  # Total images in the list
        row_element = int(images_count / 5) + 1  # Number of images in one row
        width_of_collage = 5 * 100
        height_of_collage = row_element * 100
        collage = PIL.Image.new(first_image.mode, (width_of_collage, height_of_collage))
        x_coordinate = 0
        y_coordinate = 0
        for image in self.image_array:
            collage.paste(image, (x_coordinate, y_coordinate))
            if (
                x_coordinate + 100 == width_of_collage
            ):  # If last image of the row, switch to next row
                x_coordinate = 0
                y_coordinate += 100
            else:
                x_coordinate += 100
        return collage


    def run(self):
        for f in self.inflist:
            print('chirag')
            ifile = self.zip_file.open(f)
            
            img = Image.open(ifile)

            imggray = img.convert("L")
            
            from pytesseract import Output
            # text = pytesseract.image_to_string(imggray, output_type=Output.DICT, lang="eng")
            # print(text['text'])

            data = pytesseract.image_to_data(imggray, output_type='dict', lang='eng')
            print (data)
            boxes = len(data['level'])
            vermelho = (0, 0, 255)
            for i in range(boxes):
                if self.search_keyword in data['text'][i]:
                    print(data['text'][i])
                    print(data['left'][i], data['top'][i], data['width'][i], data['height'][i], data['text'][i])
                    open_cv_image = np.array(img)
                    open_cv_image = open_cv_image[:, :, ::-1].copy()
                    cv.namedWindow('finalImg', cv.WINDOW_NORMAL)
                    cv.rectangle(open_cv_image, (data['left'][i]-20, data['top'][i]-20), (data['left'][i]+data['width'][i]+20, data['top'][i]+data['height'][i]+20), vermelho, 4)
                    # cv.imshow('acsd', open_cv_image)
                    
                    
                    '''
                    cropping the main image to show all the content along with focussed rectangle on text or image 
                    '''

                    height, width, channels  = open_cv_image.shape

                    cropped_top_row = max(data['top'][i]-500, 0)
                    cropped_bottom_row = min(data['top'][i]+data['height'][i]+500, height)
                    cropped_left_column = max(data['left'][i]-600, 0)
                    cropped_right_column = min(data['left'][i]+data['width'][i]+600, width)

                    cropped_image = open_cv_image[cropped_top_row:cropped_bottom_row, cropped_left_column:cropped_right_column] # Slicing to crop the image
                    cv.imshow("cropped_image", cropped_image)

                    # cv.imshow("finalImg",open_cv_image)
                    cv.waitKey(3000)



            # self.text_dic[ifile.name] = text['text']
            # open_cv_image = np.array(img)
            # open_cv_image = open_cv_image[:, :, ::-1].copy()
            # faces = obj.face_cascade.detectMultiScale(open_cv_image, 1.35)
            # drawing = ImageDraw.Draw(img)
            # for x, y, w, h in faces:
            #     face = img.crop((x, y, x + w, y + h))
            #     max_size = (100, 100)
            #     face.thumbnail(max_size)
            #     self.image_array.append(face)

            # collage = obj.collage_maker()
            # if collage is not None:
            #     self.image_dic[ifile.name] = collage
            # self.image_array.clear()

    def search_and_display(self):
        for key in self.text_dic:
            if self.text_dic[key].__contains__(self.search_keyword):
                print("Result found in file ", key)
                if key in self.image_dic:
                    if key == None:
                        print("But there were no faces in that file!")
                    else:
                        open_cv_image = np.array(self.image_dic[key])
                        open_cv_image = open_cv_image[:, :, ::-1].copy()
                        cv.imshow("image", open_cv_image)
                        my_uuid = uuid.uuid4()
                        cv.imwrite(f'{my_uuid}.jpg', open_cv_image)
                        cv.waitKey(3000)
                else:
                    print("But there were no faces in that file!")


    def convert_image_into_zip(self):
        shutil.make_archive("utils/zip_file", 'zip', self.images_file_dir)
        
    def convert_pdf_to_images(self):
        from pdf2jpg import pdf2jpg
        inputpath = self.file
        outputpath = ''
        result = pdf2jpg.convert_pdf2jpg(inputpath,outputpath, pages="ALL")


       
if __name__=='__main__':
    obj = ArchiveIdentifier(language="eng", search_keyword="the", file="sdg.jpg", file_format='image')
    obj.run()
    obj.search_and_display()