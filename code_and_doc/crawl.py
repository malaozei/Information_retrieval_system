import os
import re
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# 设置起始url和待访问队列
start_url = "http://www.xmu.edu.cn/"
page_pkg = [start_url]
pkg_index = 0

# 设置保存网页的文件夹
save_folder = "xmu_pages"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 设置正则表达式规则
pattern = re.compile(r"http*?xmu\.edu\.cn$")

# 定义函数，用于从队列中取出下一个链接
def get_next_url():
    global pkg_index
    if len(page_pkg) == 0:
        return None
    url = page_pkg[pkg_index]
    pkg_index+=1
    return url

# 定义函数，用于将网页保存到文件中
def save_page(url, content):
    filename = url.replace("http://", '@@@')\
            .replace("https://", "$$$")\
            .replace("/", "!!!").replace(".", "~~~")
    # @$!~
    filepath = os.path.join(save_folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# 定义函数，用于将新的链接加入队列中
def add_links_to_queue(url, soup):
    global page_pkg
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href is not None:
            href = urljoin(url, href)
            if 'xmu.edu.cn' in href:
                if href not in page_pkg:
                    page_pkg.append(href)

num=0
# 开始爬取
while True:
    url = get_next_url()
    print(url)
    if num==10000:
        break
    if url is None:
        break
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode("utf-8")
            save_page(url, content)
            num+=1
            soup = BeautifulSoup(content, "html.parser")
            add_links_to_queue(url, soup)
    except:
        pass