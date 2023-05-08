import time

import cv2
import os


def vehicle_coordinate(full_filename):
    filename = os.path.splitext(full_filename)[0]


def cut_training_image(full_filename):
    image = cv2.imread("1_20200713_153849_000030.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("hey", image)
    print(full_filename)
    time.sleep(5)

def search(dirname):
    try:
        filenames = os.listdir(dirname)

        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            if os.path.splitext(full_filename)[1] == ".jpg":
                # 파일 잘라내기 작업
                cut_training_image(full_filename)

            elif os.path.isdir(full_filename):
                search(full_filename)

    except PermissionError:
        pass


search("E:\\illegalparking\\driving_image\\Training")
