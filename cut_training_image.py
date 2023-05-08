import cv2
import os


cv2.bootstrap()

def search(dirname):
    try:
        filenames = os.listdir(dirname)

        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            if os.path.splitext(full_filename)[1] == ".jpg":
                pass

            elif os.path.isdir(full_filename):
                search(full_filename)

    except PermissionError:
        pass


search("E:\\illegalparking\\driving_image\\Training")
