import json


def getJs(filename):
    f = open(filename, 'r', encoding='Utf-8')
    for L in f:
        yield json.loads(L)

#54509个项目未能在freebase中映射
def getunItem(g,file1):
    f1 = open(file1, 'r', encoding='Utf-8')
    mid1=set()
    mid2=set()
    mid3=set()
    for l in g:
        for key in l.keys():
            if key in 'asin' :
                mid1.add(l[key])
    #print("BooksMeta:",len(mid1))
    for line1 in f1:
        line1 = line1.strip().split(",")
        mid2.add(line1[0])
    #print("ab2fb2:", len(mid2))
    for m in mid1:
        if m not in mid2:
           mid3.add(m)
           #print(m)
    print(len(mid3))

    f1.close()
    return mid3
# 54509个项目中196个项目在yago中有  共有5564（5368+196）个项目有映射 映射率为99.33%
def getreItem(mid, file):
    f = open(file, 'r', encoding='Utf-8')
    dict={}
    mid2=set()
    for line in f:
        line=line.strip().split(",")
        dict.update({line[0]: line[-1]})
    print("ab2yg:",len(dict))
    for m in mid:
        if m in dict.keys():
            mid2.add(m)
            print(m+":"+dict[m])
    print(len(mid2))





















if __name__ == '__main__':
    g=getJs("data/book/BooksMeta.json")
    mid=getunItem(g,"data/book/ab2fb2.txt")
    getreItem(mid,"data/yago/ab2yg.txt")