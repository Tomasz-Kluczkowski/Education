"""Create a module providing easy way of batch image resizing"""

import cv2
import os


def process_files(path, width, height):
    """ Automatically resize all .jpg images in directory "path" to size "width" x "height"
    parameters:
        path: (path like object)
        width: (int) width of the target image in pixels
        height: (int) height of the target image in pixels
    """
    file_list = os.listdir(path)
    for file in file_list:
        # fullname = os.path.join(path, file)
        file_name, ext = os.path.splitext(file)
        if ext == ".jpg":
            img = cv2.imread(file, 1)
            resized_img = cv2.resize(img, (width, height))
            full_name = file_name + "_resized" + ext
            cv2.imwrite(full_name, resized_img)

process_files(r"C:\Users\Kilthar\Documents\GitHub\Kilthar-s_Cave\EDUCATION\UDEMY.COM\THE PYTHON MEGA COURSE\Image "
              r"processing with OpenCV", 100, 100)

