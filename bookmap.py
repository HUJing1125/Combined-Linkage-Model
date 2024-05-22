import datetime
import gzip
import json

def getJs(filename):
    f = open(filename, 'r', encoding='Utf-8')
    for L in f:
        yield json.loads(L)


# 获取有交互数据的book元数据 59877条数据
def getIt(g, filename, filename1):
    f = open(filename, 'r', encoding='Utf-8')
    f1 = open(filename1, 'w', encoding='Utf-8')
    i = 0
    mid = set()
    mid1 = set()
    for line in f:
        line = line.strip().split(",")
        mid.add(line[0])
    print(len(mid))
    for l in g:
        for key in l.keys():
            if key in 'asin' and l[key] in mid and l[key] not in mid1:
                mid1.add(l[key])
                i += 1
                data = json.dumps(l) + '\n'  # 添加换行符分隔不同字典
                f1.write(data)
                print("Book number is :%d" % i)
                break
    print(len(mid1))
    f1.close()
    f.close()


# 根据时间戳给定范围筛选交互数据 筛选出3758132条交互数据
def selectInteraction(filename, filename1):
    # 读取CSV文件
    f = open(filename, 'r', encoding='Utf-8')
    f1 = open(filename1, 'w', encoding='Utf-8')
    index = 0
    for line in f:
        line = line.strip().split(",")
        if 1391212800 <= int(line[3]) <= 1406851199:
            index += 1
            f1.write(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "\n")
            print("Number:%d" % index)
    f1.close()
    f.close()


def selectInteraction1(filename):
    # 读取CSV文件
    f = open(filename, 'r', encoding='Utf-8')
    list = []
    dict = {}
    mid = set()
    for line in f:
        line = line.strip().split(",")
        list.append(line[0])
    print(list)
    for item_str in list:
        if item_str not in dict:
            dict[item_str] = 1
        else:
            dict[item_str] += 1
    print(dict)
    print("Selecting...")
    for key in dict.keys():
        if int(dict[key]) >= 10:
            mid.add(key)
    print(mid)
    f.close()
    return mid


# 根据交互数据大于等于10次， 二次筛选出2593035条交互数据
def selectInteraction2(mid, filename, filename1):
    f = open(filename, 'r', encoding='Utf-8')
    f1 = open(filename1, 'w', encoding='Utf-8')
    index = 0
    for line in f:
        line = line.strip().split(",")
        if line[0] in mid:
            index += 1
            f1.write(line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "\n")
    print("Number:%d" % index)
    f1.close()
    f.close()


# 确定从2014.2.1 00：00：00-2014.7.31 23：59：59时间戳
def utc_to_timestamp(utc):
    # 将UTC时间字符串转换为datetime对象
    dt = datetime.datetime.strptime(utc, '%Y-%m-%d %H:%M:%S')
    # 获取UTC时间戳
    timestamp = int((dt - datetime.datetime(1970, 1, 1)).total_seconds())
    print("UTC时间戳：", timestamp)

#5368条book数据 5368/59877*100%=8.96%
def linkage(g, filename2,filename3):
    f2 = open(filename2, 'r', encoding='utf-8')
    f3 = open(filename3, 'w', encoding='utf-8')
    i = 0
    mid = set()
    dict1: dict[str, str] = {}
    mid1 = set()
    for line in f2:
        line = line.strip().split("\t")
        dict1.update({line[0]: line[1]})
        mid.add(line[0])
    print(len(mid))
    for l in g:
        for key in l.keys():
            if key in "asin" and l[key] in mid and l[key] not in mid1:
                mid1.add(l[key])
                i += 1
                f3.write(l[key] + "," + dict1[l[key]]+","+l["title"]+"\n")
                break
    print(len(mid1))
    print("Linkage number:", i)
    f3.close()
    f2.close()


def ab2fb(filename1, filename2, filename3):
    f = gzip.GzipFile(filename1, 'r')
    f1=open(filename2, 'a', encoding='Utf-8')
    f2 = open(filename3, 'r', encoding='utf-8')
    index=0
    idx=0
    miss=set()
    i=0
    for line1 in f2:
       line1=line1.strip().split(",")
       line1[2]=line1[2]+" "+"is"
       i+=1
       print(line1[2])
       print("第%d个项目%s正在匹配" %(i, line1[0]))
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
           elif line1[1].encode() in line2[0] and line1[2].encode() in line2[2]:
               miss.add(line2[0].decode())
               f1.write(line1[0] + "," + line2[0].decode()+"\n")
               index=index+1
               print(line2)
               print("Mapping number is :", index)
               break
    f1.close()
    f.close()

def getFb(filename):
    f = gzip.GzipFile(filename, "r")
    index=0
    i: int=0
    for line in f:
        i += 1
        if i % 10000000 == 0:
            print(i, index)
        line=line.strip().split("\t".encode())
        #matchOb=re.match(r"Waiting to Exhale is".encode(), line[2], flags=re.I)
        #if matchOb is not None:
            #and "film".encode() in line[2] and "1995".encode() in line[2]:
        if "Without Remorse is".encode() in line[2]:
            print(line)
            index+=1
             #print(line)
    f.close()

def getUs(filename):
    f = open(filename, 'r', encoding='utf-8')
    mids= set()
    for line in f:
        line=line.strip().split(",")
        mids.add(line[1])
    f.close()
    print("user number:", len(mids))

if __name__ == '__main__':
    #getFb("data/freebase-rdf-latest.gz")

    #g=getJs("data/book/BooksMeta.json")
    #linkage(g, "data/book/ab2fb.txt", "data/book/ab2fb2.txt")
    #ab2fb("data/freebase-rdf-latest.gz", "data/ab2fbfinal.txt", "data/book/ab2fb2.txt")
    # getIt(g, "data/book/Books2.csv", "data/book/BooksMeta.json")
    # timestamp_to_utc("data/book/Books.csv")
    # utc_to_timestamp('2014-07-31 23:59:59')
    # mid=selectInteraction1("data/book/Books1.csv")
    # selectInteraction2(mid, "data/book/Books1.csv", "data/book/Books2.csv")
    getUs("data/book/Books2.csv")

