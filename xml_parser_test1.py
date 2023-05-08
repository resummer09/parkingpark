import xml.etree.ElementTree as et
import os


def search_for_vehicle(objects):
    coordinate = []

    for data in objects:
        if data.tag == "name" and "Vehicle" not in data.text:
            break

        else:
            pass

        if data.tag == "bndbox":
            coordinate = parse_coordinate(data)

    return coordinate


def parse_coordinate(vehicle):
    xmin, ymin, xmax, ymax = "", "", "", ""

    for coordinate in vehicle:
        coortag = coordinate.tag
        coortext = coordinate.text

        if coortag == "xmin":
            xmin = coortext

        elif coortag == "ymin":
            ymin = coortext

        elif coortag == "xmax":
            xmax = coortext

        elif coortag == "ymax":
            ymax = coortext

    bndbox = [xmin, ymin, xmax, ymax]

    return bndbox


def xml_parsing(full_filename):
    result = []
    try:
        tree = et.parse(full_filename)
        root = tree.getroot()

        for child in root:
            if child.tag == "object":
                bndbox = search_for_vehicle(child)
                if bndbox:
                    result.append(bndbox)

        return result

    except et.ParseError:
        print(f"ParseErrorOccurred.")
        return []


# Check whether the target is training data or validation data and change the folder name appropriately.
def make_dir():
    path = "E:\\illegalparking\\driving_image\\Validation"
    label_path = f"{path}\\label"
    image_path = f"{path}\\image"

    os.chdir(path)

    if not os.path.exists(label_path):
        os.mkdir(label_path)

    if not os.path.exists(image_path):
        os.mkdir(image_path)


# Check whether the target is training data or validation data and change the folder name appropriately.
# Choose between Validation or Training
def make_csv(filename, results):
    path = "E:\\illegalparking\\driving_image\\Validation\\label"
    csv_filename = f"{os.path.splitext(filename)[0]}.csv"

    f = open(f"{path}\\{csv_filename}", "w", encoding="UTF-8")
    f.write("xmin, ymin, xmax, ymax \n")

    for result in results:
        f.write(f"{result[0]}, {result[1]}, {result[2]}, {result[3]}\n")

    f.close()


def search(dirname):
    make_dir()
    try:
        filenames = os.listdir(dirname)

        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            if os.path.splitext(full_filename)[1] == ".xml":
                results = xml_parsing(full_filename)

                if results is not []:
                    make_csv(filename, results)

            elif os.path.isdir(full_filename):
                search(full_filename)

    except PermissionError:
        pass


search("E:\\illegalparking\\driving_image\\Validation")
