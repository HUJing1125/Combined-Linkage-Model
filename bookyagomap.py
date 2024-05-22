import json
import re
def find_between(s):
    match = re.search(r'\((\s*\d{4}\s*)', s)

    # 如果找到了匹配项，提取它
    if match:
        # match.group(1)会获取括号内第一个分组的内容，即年份
        year = match.group(1).strip()  # 使用strip()去除可能存在的空格
        return year  # 输出: 1986
    else:
        return ""
def getJs(filename):
    f = open(filename, 'r', encoding='Utf-8')
    for L in f:
        yield json.loads(L)

def ab2yg(g,filename2,filename3):
    f2=open(filename2, 'r', encoding='Utf-8')
    f3=open(filename3, 'w', encoding='Utf-8')
    i = 0
    dict = {}
    for l in g:
        dict.update({l["asin"]:l["title"]})
    for line2 in f2:
        line3 = line2.strip().replace('http://yago-knowledge.org/resource/', '').replace('__','')
        for key in dict.keys():
            if line3 in dict[key]:
                i+=1
                f3.write(key +","+dict[key]+ ","+ line2)
                break
    print("Linkage number:", i)
    f3.close()
    f2.close()

def find_duplicates(filepath):
    f = open(filepath, 'r', encoding='Utf-8')
    lines=[]
    lines1=[]
    for line in f:
        line=line.strip().split(",")
        if line[0] not in lines:
            lines.append(line[0])
        else:
            lines1.append(line[0])
            print(line)
    print("repeat number:", len(lines1))
    print("No number:", len(lines))
    f.close()

def transform(filename,filename1):
    f = open(filename, 'r', encoding='Utf-8')
    f1=open(filename1,'w',  encoding='Utf-8')
    i=0
    for line in f:
        line=line.strip()
        line=line.replace('_','  ').replace('  ',' ').replace(u' u0028','(').replace(u' u0029',')').replace(u' u0027',"'").replace(u' u003A',':').replace(u' u002E', '.').replace(u' u0021', '!').replace(u' u00BD', '½').replace(u' u002C',',').replace(u' u2013','-').replace(u' u002F','/').replace(u' u0026','&').replace(u' u003F','?').replace(u' u0024','$').replace(u' u002B','+').replace(' s','s')
        i+=1
        f1.write(line+"\n")
    print("number:", i)
    f1.close()
    f.close()

def sort(filename):
        # 读取文件内容，并解析出ID和对应的行
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # 解析ID和行内容，假设ID是每行的第一个字段
        id_lines = [(int(line.split(",")[0]), line) for line in lines if line.strip()]

        # 按ID排序
        sorted_id_lines = sorted(id_lines, key=lambda x: x[0])

        # 提取排序后的文件内容
        sorted_content = [line[1] for line in sorted_id_lines]

        # 将排序后的内容写回到文件
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(sorted_content)

def ab2yg1(g,filename2,filename3):
    f2=open(filename2, 'r', encoding='Utf-8')
    f3=open(filename3, 'w', encoding='Utf-8')
    i = 0
    dict = {}
    for l in g:
        dict.update({l["asin"]:l["title"]})
    for line2 in f2:
        line2 = line2.strip().split(",")
        line3=line2[1].replace('-','')
        print(line3)
        for key in dict.keys():
            if line3 == key:
                i+=1
                f3.write(key +","+dict[key]+ ","+ line2[0]+"\n")
                break
    print("Linkage number:", i)
    f3.close()
    f2.close()

def ab2yg2(g,filename2,filename3):
    f2=open(filename2, 'r', encoding='Utf-8')
    f3=open(filename3, 'w', encoding='Utf-8')
    i = 0
    dict = {}
    for l in g:
        dict.update({l["asin"]:[l["title"],l["brand"]]})
    for line2 in f2:
        line2 = line2.strip().split(",")
        line3=line2[0].replace('http://yago-knowledge.org/resource/', '').replace('_','  ').replace('  ',' ').replace(u' u0028','(').replace(u' u0029',')').replace(u' u0027',"'").replace(u' u003A',':').replace(u' u002E', '.').replace(u' u0021', '!').replace(u' u00BD', '½').replace(u' u002C',',').replace(u' u2013','-').replace(u' u002F','/').replace(u' u0026','&').replace(u' u003F','?').replace(u' u0024','$').replace(u' u002B','+').replace(' s','s')
        line4=line2[1].replace('_',' ').replace(u' u0028','(').replace(u' u0029',')')
        line4 = re.sub(r'\(.*?\)', '', line4).replace('http://yago-knowledge.org/resource/', '')
        for key in dict.keys():
            if line3 in dict[key][0] and line4 in dict[key][1]:
                i+=1
                f3.write(key +","+dict[key][0]+","+line2[0]+"\n")
                break
    print("Linkage number:", i)
    f3.close()
    f2.close()
if __name__ == '__main__':
    #g = getJs("data/book/BooksMeta.json")
    #ab2yg2(g, "data/yago/author.csv", "data/yago/ab2yg2.txt")
    #sort("data/yago/ab2yg.txt")
    find_duplicates("data/yago/ab2yg.txt")
    #transform("data/yago/bookquery-result.csv", "data/yago/bookquery-result1.txt")

#ab2yg 219