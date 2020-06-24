# -*- coding: utf-8 -*-
# Created by: ERMAC
# Created data: 2020/6/24
# 去除Srt字幕文件中非中文字幕

def is_alphabet(ch):
    if (u"\u0041" <= ch <= u"\u005a") or (u"\u0061" <= ch <= u"\u007a"):
        return True
    else:
        return False


def is_chinese(ch):
    for i in ch:
        if u'\u4e00' <= i <= u'\u9fff':
            return True
    return False


def covertsub_out(inputname):
    f = open(inputname, "r", encoding="UTF-8")
    fo = open(inputname[:-4] + "_out.srt", "w", encoding="UTF-8")
    lines = f.readlines()
    for line in lines:
        if len(line) > 5 and not is_chinese(line) and \
                (is_alphabet(line[2]) or is_alphabet(line[3]) or is_alphabet(line[4]) or is_alphabet(line[5])):
            pass
        else:
            fo.write(line)
    fo.close()
    f.close()

    print("完成！")


if __name__ == "__main__":
    inputname = input("输入文件名：")
    covertsub_out(inputname)