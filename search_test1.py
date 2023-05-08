import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            if "[원천]도심로" == filename:
                os.chdir(dirname)
                os.rename(filename, "image_downtown")
                filename = "image_downtown"

            elif "[라벨]도심로" == filename:
                os.chdir(dirname)
                os.rename(filename, "label_downtown")
                filename = "label_downtown"

            elif "[원천]자동차전용도로" == filename:
                os.chdir(dirname)
                os.rename(filename, "image_motorway")
                filename = "image_motorway"

            elif "[라벨]자동차전용도로" == filename:
                os.chdir(dirname)
                os.rename(filename, "label_motorway")
                filename = "label_motorway"

            elif "자동차전용도로" == filename:
                os.chdir(dirname)
                os.rename(filename, "motorway")
                filename = "motorway"

            elif "도심로" == filename:
                os.chdir(dirname)
                os.rename(filename, "downtown")
                filename = "downtown"

            elif "맑음" == filename:
                os.chdir(dirname)
                os.rename(filename, "sunny")
                filename = "sunny"

            elif "강우" == filename:
                os.chdir(dirname)
                os.rename(filename, "rainy")
                filename = "rainy"

            elif "안개" == filename:
                os.chdir(dirname)
                os.rename(filename, "foggy")
                filename = "foggy"

            elif "주간일출" == filename:
                os.chdir(dirname)
                os.rename(filename, "day")
                filename = "day"

            elif "야간일몰" == filename:
                os.chdir(dirname)
                os.rename(filename, "night")
                filename = "night"

            elif "전방" in filename:
                os.chdir(dirname)
                os.rename(filename, filename.replace("전방", "front"))
                filename = filename.replace("전방", "front")

            elif "측방(전측방)" in filename:
                os.chdir(dirname)
                os.rename(filename, filename.replace("측방(전측방)", "side"))
                filename = filename.replace("측방(전측방)", "side")

            elif "측방(후측방)" in filename:
                os.chdir(dirname)
                os.rename(filename, filename.replace("측방(후측방)", "side"))
                filename = filename.replace("측방(후측방)", "side")

            elif "라벨링데이터" == filename:
                os.chdir(dirname)
                os.rename(filename, filename.replace("라벨링데이터", "label"))
                filename = filename.replace("라벨링데이터", "label")

            elif "원천데이터" in filename:
                os.chdir(dirname)
                os.rename(filename, filename.replace("원천데이터", "image"))
                filename = filename.replace("원천데이터", "image")

            full_filename = os.path.join(dirname, filename)

            # 폴더면 들어가서 더 해
            if os.path.isdir(full_filename):
                # 진행도 확인
                print(full_filename)

                search(full_filename)

    except PermissionError:
        pass


search("e:\\illegalparking\\driving_image\\Validation")
