import os
import pandas




if __name__ == "__main__":
    # キャラクタ情報を読み込み
    CHARA_TXT_PATH = "characters.txt"
    RNAME_TXT_PATH = "represent_name.txt"
    f = open(CHARA_TXT_PATH, "r")
    represent_names = open(RNAME_TXT_PATH, "r")
    represent_names = represent_names.read().splitlines()


    chara_list = []
    for line in f.readlines():
        line=line.strip()#末尾の改行を除去、
        line=line.split("\n")# 改行までをリスト化.
        chara_list.append(line)
    
    print(chara_list)

    paragraph = []
    story = []
    for chara_names, rname in enumerate(chara_list, represent_names):
        for name in chara_names:
            for i, paragraph in enumerate(story):
                for j, sentence in enumerate(paragraph):
                    if name in sentence:
                        print("{}段落目の{}文目に{}がいます．".format((i+1), (j+1), rname))


    

