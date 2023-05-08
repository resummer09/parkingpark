import time

import cv2
import os
import csv


class IlligalParkingLearning:

    def __init__(self):
        self.image = None

    def cut_training_image(self, coordinate):
        xmin, ymin, xmax, ymax = int(coordinate[0]), int(coordinate[1]), int(coordinate[2]), int(coordinate[3])
        vehicle_image = self.image[ymin:ymax, xmin:xmax]

        # 학습시켜
        print("xmin=", xmin, "ymin=", ymin, "xmax=", xmax, "ymax=", ymax)
        cv2.imshow("training_image", vehicle_image)
        cv2.waitKey(1000)

    def vehicle_coordinate(self, image_filename):
        path = "E:\\illegalparking\\driving_image\\Training\\label\\"
        filename = os.path.splitext(image_filename)[0].split("\\")[-1]
        full_filename = f"{path}{filename}_v001_1.csv"
        f = open(full_filename, "r", encoding="utf-8")
        rdr = csv.reader(f)
        for line in rdr:
            if "xmin" in line:
                pass
            else:
                self.cut_training_image(line)

    def load_training_image(self, full_filename):
        self.image = cv2.imread(full_filename, cv2.IMREAD_COLOR)
        self.vehicle_coordinate(full_filename)

    def search(self, dirname):
        try:
            filenames = os.listdir(dirname)

            for filename in filenames:
                full_filename = os.path.join(dirname, filename)

                if os.path.splitext(full_filename)[1] == ".jpg":
                    # 파일 잘라내기 작업
                    self.load_training_image(full_filename)

                elif os.path.isdir(full_filename):
                    self.search(full_filename)

        except PermissionError:
            pass


illegal = IlligalParkingLearning()
illegal.search("E:\\illegalparking\\driving_image\\Training")