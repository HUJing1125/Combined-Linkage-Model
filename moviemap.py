#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import gzip
import re
from typing import List

def getIt(mids, filename, filename1):
    f = open(filename, 'r', encoding='utf-8')
    f2 = open(filename1, 'w', encoding='utf-8')
    midss=set()
    for line in f:
        line=line.strip().split("::")
        if not int(line[0]) in mids:
            continue
        line[1]=line[1].replace("(", ",").replace(")", "")
        f2.write(line[0]+","+line[1]+"\n")
        midss.add(line[0]+line[1])
    f2.close()
    f.close()
    print("item number:", len(midss))
    return midss


def getUs(filename, filename1):
    f = open(filename, 'r', encoding='utf-8')
    f2 = open(filename1, 'w', encoding='utf-8')
    mids= set()
    for line in f:
        line=line.strip().split("::")
        if int(line[2])==1:
            continue
        mids.add(int(line[0]))
        f2.write(line[0]+" "+line[1]+" "+line[2]+" "+line[3]+"\n")
    f2.close()
    f.close()
    print("user number:", len(mids))
    return mids

def getRa(mids, filename, filename1):
    f = open(filename, 'r', encoding='utf-8')
    f1 = open(filename1, 'w', encoding='utf-8')
    mids1=set()
    midd=set()
    for line in f:
        line=line.strip().split("::")
        if not int(line[0]) in mids:
            continue
        if int(line[2])>=4:
            line[2] = 1
        elif int(line[2])==3:
            line[2] = 0
        else:
            continue
        mids1.add(int(line[1]))
        midd.add(str(line))
        f1.write(line[0] + " " + str(line[1]) + " " + str(line[2]) + "\n")
    f1.close()
    f.close()
    print("ratings number:", len(midd))
    return mids1



def getFb(filename):
    f = gzip.GzipFile(filename, "r")
    mids = set()
    i: int=0
    for line in f:
        line=line.strip().split("\t".encode())
        #matchOb=re.match(r"Waiting to Exhale is".encode(), line[2], flags=re.I)
        #if matchOb is not None:
            #and "film".encode() in line[2] and "1995".encode() in line[2]:
        if "<http://rdf.freebase.com/ns/m.0676dr>".encode() in line[0] and re.search(r"Grumpier Old Men".encode(), line[2], flags=re.IGNORECASE):
            print(line[0])
            print(line)
            break
             #print(line)
            #
        #else:
            #print("wait...")
    f.close()
    return mids

def linkage(filename1, filename2, filename3):
    f1 = open(filename1, 'r', encoding='utf-8')
    f2 = open(filename2, 'r', encoding='utf-8')
    f3 = open(filename3, 'w', encoding='utf-8')
    i=0
    dict={}
    dict1={}
    for line1 in f1:
        line1 = line1.strip().split(",")
        dict.update({line1[0]: [line1[1].strip(), line1[-1]]})
    for line2 in f2:
        line2 = line2.strip().split("\t")
        dict1.update({line2[0]: line2[1]})
    for key in dict.keys():
      if key in dict1.keys():
        f3.write(key+","+dict1[key]+","+dict[key][0]+","+dict[key][1] + "\n")
        i+=1
    print("Linkage number:", i)
    f3.close()
    f2.close()
    f1.close()

def getEn(filename):
    f = open(filename, 'r', encoding='Utf-8')
    mids = []
    for line in f:
        line = line.strip().split(",")
        mids.append("<http://rdf.freebase.com/ns/" + line[1] + ">")
    f.close()
    print("en: ", len(mids))
    return mids

def getNa(filename):
    f = open(filename, 'r', encoding='Utf-8')
    midss = set()
    for line in f:
        line = line.strip().split(",")
        midss.add(line[2].encode())
    f.close()
    print("en: ", len(midss))
    return midss
#RV algorithm
def ml2fb(filename1,filename2,filename3):
    f = gzip.GzipFile(filename1, 'r')
    f1=open(filename2, 'a', encoding='Utf-8')
    f2=open(filename3, 'r', encoding='Utf-8')
    index=0
    idx=0
    miss=set()
    start_line=198
    for _ in range(start_line - 1):
        next(f2)
    for line1 in f2:
        line1=line1.strip().split(",")
        print("第%s个项目%s正在匹配" %(line1[0], line1[2]))
        f.seek(0)
        for line in f:
           idx += 1
           if idx % 100000000 == 0:
              print(idx, index)
           line = line.strip()
           if "<http://rdf.freebase.com/ns/".encode() not in line:
              continue
           else:
               line2 = line.split("\t".encode())
           if line2[0].decode() in miss:
              continue
           elif line1[1].encode() in line2[0] and line1[2].encode() in line2[2] and line1[3].encode() in line2[2]:
               miss.add(line2[0].decode())
               f1.write(line1[0] + "," + line2[0].decode()+"\n")
               index=index+1
               print("Mapping number is :", index)
               break
    f1.close()
    f.close()
    f2.close()

def getFinall(miss,filename,filename1):
    f = open(filename, 'r', encoding='Utf-8')
    f1 = open(filename1, 'w', encoding='utf-8')
    for line in f:
        line=line.strip().split(",")
        if line[1] in miss:
            f1.write(line[0]+","+line[1])
    f1.close()
    f.close()


def find_duplicates(filepath):
    f = open(filepath, 'r', encoding='Utf-8')
    lines=[]
    for line in f:
        line=line.strip().split(",")
        if line[2].strip() not in lines:
            lines.append(line[2].strip())
        else:
            print(line[2])
    print(len(lines))
    #print(lines)


if __name__ == '__main__':

    #mids = getFb("data/freebase-rdf-latest.gz")

   # mids2=getUs("data/ml-1m/users.dat", "data/ml-1m/users1.txt")
    #mids3=getRa(mids2, "data/ml-1m/ratings.dat", "data/ml-1m/ratings1.txt")
    #mids = getIt(mids3, "data/ml-1m/movies.dat", "data/ml-1m/movie1.txt")
     #linkage("data/movie1.txt", "data/ml-1m/ml2fb.txt", "data/ml-1m/ml2fb2.txt")

    #mids=getEn("data/ml-1m/ml2fb2.txt")
    #midss=getNa("data/ml-1m/ml2fb2.txt")
    ml2fb("data/freebase-rdf-latest.gz", "data/ml-1m/ml2fbfinal.txt", "data/ml-1m/ml2fb2.txt")
    #getFinall(mis, "data/ml-1mml2fb2.txt", "data/ml-1m/ml2fbfinal.txt")

    #find_duplicates("data/ml-1m/movie1.txt")