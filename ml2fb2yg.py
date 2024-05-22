

#40个项目未能在freebase中映射
def getunItem(file1,file2):
    f1 = open(file1, 'r', encoding='Utf-8')
    f2 = open(file2, 'r', encoding='utf-8')
    mid1=set()
    mid2=set()
    mid3=set()
    for line1 in f1:
        line1=line1.strip().split(",")
        mid1.add(line1[0])
    print("movie1:",len(mid1))
    for line2 in f2:
        line2 = line2.strip().split(",")
        mid2.add(line2[0])
    print("ml2fb2:", len(mid2))
    for m in mid1:
        if m not in mid2:
           mid3.add(m)
    print(mid3)
    print(len(mid3))

    f2.close()
    f1.close()
    return mid3
# 40个项目中16个项目在yago中有  共有3598（3582+16）个项目有映射 映射率为99.33%
def getreItem(mid, file):
    f = open(file, 'r', encoding='Utf-8')
    dict={}
    mid2=set()
    for line in f:
        line=line.strip().split(",")
        dict.update({line[0]: line[2]})
    print("ml2yg:",len(dict))
    for m in mid:
        if m in dict.keys():
            mid2.add(m)
            print(m+":"+dict[m])
    print(len(mid2))





















if __name__ == '__main__':

    mid=getunItem("data/ml-1mmovie1.txt","data/ml-1m/ml2fb2.txt")
    getreItem(mid,"data/yago/ml2yg.txt")