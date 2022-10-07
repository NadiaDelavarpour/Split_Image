import cv2
import os
from PIL import Image

def split(rows, cols, path_to_image):
    #number of rows and column you want to split your image
    #the exact directory to the image
    im = Image.open(path_to_image)
    im_width, im_height = im.size

    row_width = (im_width / rows)
    row_height = (im_height / cols)
    n = 0
    for i in range(0, cols):
        for j in range(0, rows):
            box = (j * row_width, i * row_height, j * row_width +
                   row_width, i * row_height + row_height)
            outp = im.crop(box)
            name, ext = os.path.splitext(path_to_image)
            outp_path = name + "_" + str(n) + ext
            print("Exporting image tile: " + outp_path)
            outp.save(outp_path)
            n += 1




path_to_image ='D:/Image/Split_Test/C0002_Raw_Image000145.jpg'
im = cv2.imread(path_to_image)
split(5, 3, path_to_image)