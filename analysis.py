import os
import itertools
import glob
from tqdm import tqdm


def has_introdcution(line):
    if "******" in line or "改訂版" in line:
        return True
    else:
        return False

def has_charainfo(line):
    if "†††††" in line:
        return True
    else:
        return False

def extract_story(txt_path):
    f = open(txt_path, "r")
    story = []
    paragraph = []
    for line in f.readlines():
        line=line.strip()#末尾の改行を除去、
        line=line.split("\n")# 改行までをリスト化.

        # あらすじかどうか判定
        if has_introdcution(line[0]):
            paragraph =  []
            continue
        # 登場人物紹介か判定
        if has_charainfo(line[0]):
            break

        # 空行かどうか
        if  line == ['']:
            if len(paragraph) == 0:
                continue
            else:
                # これまでの文章を段落としてstoryに保存．
                story.append(paragraph)
                paragraph = []
        else:
            # 文章を段落として追加
            paragraph.append(line[0])
    return story

def find_chara_pairs(novel_path, chara_list, represent_names,csv_path):
    story = extract_story(novel_path)
    for p_num, paragraph in enumerate(story):
        chara_in_paragraph = []
        for s_num, sentence in enumerate(paragraph):
            for chara_names, rname in zip(chara_list, represent_names):
                for name in chara_names:
                    if name in sentence:
                        chara_in_paragraph.append(rname)
                        # print("{}段落目の{}文目に{}がいます．".format((p_num+1), (s_num+1), rname))
                        break
                    else:
                        continue
        

        chara_pairs = list(set(list(itertools.combinations(list(set(chara_in_paragraph)),2))))
        # 段落内にペアがない場合は次のループへ
        if len(chara_pairs) == 0:
            continue
        # 段落内にペアがあったらcsvに記述する．
        else:    
            for chara_pair in chara_pairs:    
                with open(csv_path, "a") as f:
                    f.write("{},{},{}".format(os.path.basename(novel_path),chara_pair[0],chara_pair[1]) + "\n")

def load_chara_data(CHARA_TXT_PATH, RNAME_TXT_PATH):
    f = open(CHARA_TXT_PATH, "r")
    chara_list = []
    for line in f.readlines():
        line=line.strip()#末尾の改行を除去、
        line=line.split(",")# 改行までをリスト化.
        chara_list.append(line)
    
    represent_names = open(RNAME_TXT_PATH, "r")
    represent_names = represent_names.read().splitlines()
    return chara_list, represent_names



  




if __name__ == "__main__":
    # txtデータ読み込み
    # キャラクタ情報を読み込み
    CHARA_TXT_PATH = "characters.txt"
    RNAME_TXT_PATH = "represent_name.txt"

    # データ保存のcsv_path
    CSV_PATH = "v2.csv"
    # csv作成
    with open(CSV_PATH, "w") as f:
        f.write("filename,chara_a,chara_b\n")

    chara_list, represent_names = load_chara_data(CHARA_TXT_PATH, RNAME_TXT_PATH)
    novel_path_list = sorted(glob.glob("./novel-txts/*.txt"))
    for novel_path in tqdm(novel_path_list):
        # ペアを探す
        find_chara_pairs(novel_path, chara_list, represent_names, CSV_PATH)


    