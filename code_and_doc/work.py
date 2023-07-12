import tkinter as tk
from PIL import Image, ImageTk
import math

inverindex = {}# 一个字典，键是关键词，值是很多二元列表，列表有序，列表中放着网址和df
stop_word = []

def get_inverindex():
    with open('inverindex.txt', 'r', encoding='utf8') as fp:
        lines = fp.readlines()
        i = 0
        while i < len(lines):
            k = lines[i].replace("\n", '')
            inverindex[k] = {}
            while True:
                i += 1
                w = lines[i].replace('\n', '')
                if w == 'SSSSTTTTOOOOPPPP':
                    break
                i += 1
                f = int(lines[i])
                inverindex[k][w] = f
            i += 1

def get_stop_word():
    file = open('stop.txt', 'r', encoding='utf8')
    words = file.readlines()
    for word in words:
        word = word.strip()
        stop_word.append(word)
    file.close()

def trans_inverindex_to_sorted_list():
    for k, v in inverindex.items():
        inverindex[k] = list(v.items())
        inverindex[k] = sorted(inverindex[k], key=lambda x: -x[1])

def search_word(word):
    if word in stop_word:
        return [('it is a stop word', -1)]
    if word not in inverindex:
        return [('nothing matched', -1)]
    return inverindex[word]

def get_item_from_tuple_in_list(results0):
    result = []
    for result0 in results0:
        result.append(result0[0])
    return result

class MyButton:
    def __init__(self, canvas, x, y, width, height, text, command):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.command = command
        
        # 创建按钮的外框
        # self.rectangle = self.canvas.create_rectangle(
        #     self.x, self.y, self.x + self.width, self.y + self.height,
        #     fill="gray", outline="black"
        # )

        self.rectangle = self.canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height,
            fill="black", outline="black"
        )
        
        # 创建按钮的文本标签
        self.label = self.canvas.create_text(
            self.x + self.width / 2, self.y + self.height / 2,
            text=self.text, fill="white", font=("Arial", 12)
        )
        
        # 绑定按钮的点击事件
        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.label, "<Button-1>", self.on_click)
        
    def on_click(self, event):
        if self.command is not None:
            self.command()

class InfoRetrievalUI:
    # and_opertaion,or_operation,not_operration分别是三种操作符的按钮
    # display是显示结果的函数，clear_result对现有的关键词和文件检索结果清空
    # sort_files在输出之前进行排序
    def __init__(self):
        self.result_files = []
        self.keywords = []
        self.logic_op = None
        
        self.root = tk.Tk()
        self.root.title("Information Retrieval System")

        self.canvas = tk.Canvas(self.root, width=1300, height=600)
        self.canvas.pack()
        self.image = Image.open("information.jpg").resize((1300, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")

        self.root.config(bg='white')  # 设置UI的背景颜色为蓝色
        self.root.geometry("1300x600")  # 设置UI的大小为1000x600
        
        self.input_frame = self.canvas.create_rectangle(10, 10, 180, 70, fill="white", outline="white")
        self.input_label = self.canvas.create_text(25, 20, text="Input", anchor="nw")
        self.input_entry = tk.Entry(self.root)
        self.canvas.create_window(20, 40, window=self.input_entry, anchor="nw")
        
        self.button_frame = self.canvas.create_rectangle(10, 90, 980, 140, fill="white", outline="white")
        self.display_button = MyButton(self.canvas, 20, 100, 150, 30, "Display Result", self.display_result)
        self.and_button = MyButton(self.canvas, 200, 100, 80, 30, "AND", self.and_operation)
        self.or_button = MyButton(self.canvas, 300, 100, 80, 30, "OR", self.or_operation)
        self.not_button = MyButton(self.canvas, 400, 100, 80, 30, "NOT", self.not_operation)
        self.clear_button = MyButton(self.canvas, 500, 100, 150, 30, "Clear Result", self.clear_result)
        
        self.result_frame = self.canvas.create_rectangle(10, 160, 980, 590, fill="white", outline="white")
        self.result_label = self.canvas.create_text(25, 170, text="Search Result:", anchor="nw")
        self.result_text = tk.Text(self.root, height=30, width=120)
        self.canvas.create_window(20, 190, window=self.result_text, anchor="nw")
        
    def run(self):
        self.root.mainloop()
        
    def display_result(self):
        keywords = self.input_entry.get()
        self.result_files = get_item_from_tuple_in_list(self.search_files(keywords))
        self.keywords = [keywords]
        self.display_files(self.result_files)
        self.logic_op = None
        
    def and_operation(self):
        if self.result_files:
            keywords = self.input_entry.get()
            new_files = get_item_from_tuple_in_list(self.search_files(keywords))
            self.result_files = list(set(self.result_files) & set(new_files))
            self.keywords = list(set([keywords])&set(self.keywords))
            self.display_files(self.result_files)
            self.logic_op = "AND"
        
    def or_operation(self):
        if self.result_files:
            keywords = self.input_entry.get()
            new_files = get_item_from_tuple_in_list(self.search_files(keywords))
            self.result_files = list(set(self.result_files) | set(new_files))
            self.keywords = list(set(set([keywords]))|set(self.keywords))
            self.display_files(self.result_files)
            self.logic_op = "OR"
        
    def not_operation(self):
        if self.result_files:
            keywords = self.input_entry.get()
            new_files = get_item_from_tuple_in_list(self.search_files(keywords))
            self.result_files = list(set(self.result_files) - set(new_files))
            self.keywords = list(set(self.keywords)-set([keywords]))
            self.display_files(self.result_files)
            self.logic_op = "NOT"
        
    def clear_result(self):
        self.result_files = []
        self.display_files(self.result_files)
        self.keywords = []
        self.logic_op = None
        
    def sort_files(self, files):# 对结果进行排序
        file_scores=[[file ,0] for file in files]
        for keyword in self.keywords:# 每个词
            for file_score in file_scores:# 一个文件
                for k, v in inverindex[keyword]:# 倒排索引表中取出该单词对应的所有文件
                    if file_score[0] == k:
                        # 如果一个单词出现的文档中包含当前这篇文档，那么这篇文档就加上该单词在文档中出
                        # 现的对数频次，这样就可以计算一个词汇的相关度
                        file_score[1] += math.log10(v)
        file_scores = sorted(file_scores, key=lambda x:-x[1])
        return file_scores

    def display_files(self, files):
        self.result_text.delete("1.0", tk.END)
        if files[0]=='it is a stop word' or files[0]=='nothing matched':
            self.result_text.insert(tk.END, files[0] + "\n")     
            return
        self.result_text.insert(tk.END, '共有' + str(len(files)) + '个文件' + "\n")
        self.result_text.insert(tk.END, '以下是经过排序后的内容\n')
        if len(files) != 1:
            files=self.sort_files(files)
        for file in files:
            self.result_text.insert(tk.END, file[0] + "\n")
        
    def search_files(self, word):
        if word in stop_word:
            return [('it is a stop word',-1)]
        if word not in inverindex:
            return [('nothing matched',-1)]
        return inverindex[word]
    
if __name__ == "__main__":
    get_stop_word()
    get_inverindex()
    trans_inverindex_to_sorted_list()
    ui = InfoRetrievalUI()
    ui.run()