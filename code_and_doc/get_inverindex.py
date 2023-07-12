import glob
import jieba
import re 
import os
pattern = re.compile("[^\u4e00-\u9fa5]")  # 匹配所有非汉字字符
file_paths = glob.glob('D:\\class\\大二小\\智能信息检索\\crawl1\\code\\xmu_pages\\*')
inverindex={}#倒排索引表
stop_word = []

def get_stop_word():
    file = open('stop.txt', 'r', encoding='utf8')
    words = file.readlines()
    for word in words:
        word = word.strip()
        stop_word.append(word)
    file.close()

def process(text, id):
    id=id.replace('@@@', "http://")\
        .replace("$$$", "https://")\
            .replace("!!!", "/")\
                .replace("~~~", ".")
    text = re.sub(pattern, "", text)    # 将非汉字字符替换为空字符串
    words=jieba.cut(text)
    for word in words:
        if word in stop_word:
            continue
        if word in inverindex:
            if id in inverindex[word]:
                inverindex[word][id]=inverindex[word][id]+1
            else:
                inverindex[word][id]=1
            continue
        inverindex[word]={}
        inverindex[word][id]=1

def get_the_inverindex_table():
    print('begin to get the inverindex table')
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf8') as file:
            content = file.read()
            process(content,os.path.basename(file_path))
    print('get over')

def write_inverindex_to_file():
    #把倒排索引表写进文件result.txt
    print('begin to write the inverindex table')
    with open('inverindex.txt', 'w', encoding='utf8') as file:
        for k,v in inverindex.items():#v是一个列表，里面是很多元组
            file.write(k+'\n')
            for vv in v:
                file.write(str(vv[0])+'\n'+str(vv[1])+'\n')
            file.write('SSSSTTTTOOOOPPPP\n')
    print('write over')

get_stop_word()
get_the_inverindex_table()
write_inverindex_to_file()