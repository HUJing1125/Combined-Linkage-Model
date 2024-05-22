#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import gzip

from typing import List


def check(mid, mids):
    if mid.decode() in mids:
        return 1
    else:
        return 0


# 从freebase中获取在映射对文件中有的MID的三元组信息组成子图
def getSub(mids, filename2, filename3):
    f = gzip.GzipFile(filename2, "r")
    f2 = open(filename3, 'w', encoding='utf-8')
    idx = 0
    idx2 = 0
    for line in f:
        idx += 1
        if idx % 1000000 == 0:
            print(idx, idx2)
        line = line.strip()
        if "<http://rdf.freebase.com/ns/".encode() not in line:
            continue
        line2 = line.split("\t".encode())
        if check(line2[0], mids) or check(line2[2], mids):
            f2.write(line.decode() + "\n")
            idx2 += 1
    f2.close()
    f.close()


# 获取映射对文件中的MID到mids中
def getEn(filename):
    f = open(filename, 'r', encoding='Utf-8')
    mids = set()
    for line in f:
        line = line.strip().split(",")
        mids.add("<http://rdf.freebase.com/ns/" + line[1] + ">")
    f.close()
    print("en: ", len(mids))
    return mids


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("usage: python getSub3.py enfile freebase subbase")
        sys.exit(-1)
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    filename3 = sys.argv[3]
    mids = getEn(filename1)
    getSub(mids, filename2, filename3)

