# Information_retrieval_system
一个本地信息检索系统
爬取网页以后，在本地进行布尔检索的系统。
效果如下：
1.	进行单个关键词进行检索：
关键词：厦门
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/8aee296e-4280-496c-aad3-6f352e906a4a)

2.	进行多关键词与操作：
关键词：厦门&大学&河南
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/b162eb64-3dc8-408f-a33f-ec101c1db79d)

显然检索结果变少了，符合布尔检索的规律。
3.	多关键词或操作：
关键词：河南 or 河北 or 教育
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/665f603c-a55a-40d4-b406-7f8d4656eb95)
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/6ae29d17-bac0-4a33-b6bf-353e60f18807)
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/25eb8080-920a-4feb-83a0-8ba5d2ddadc7)

检索结果不断增多，符合逻辑运算的逻辑。
4.	多关键词非操作：
教育 not 厦门
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/398f12bd-3f31-48a3-b749-9d527e9d6d16)
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/3ad9a4ed-9e8b-4d97-8780-3e520d1f1bf0)

结果不断变少，符合逻辑。
5.	多关键词混合操作：
教育or 爱国 and 大学 not 厦门
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/4a2ab548-39fb-488f-a6f0-e4e3085ba7c7)
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/154242a4-6a71-40d8-b9a1-3f8c552805a6)
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/f19d4e46-409c-4d32-8254-995f9429346f)
![image](https://github.com/malaozei/Information_retrieval_system/assets/94264539/1b83dbdb-a1b6-4516-8510-926509e70f16)

   
# 使用方法：
先用crawl.py文件爬取网页，再用get_inverindex.py获取倒排索引表，随后可以用work.py进行工作。
环境配置的要求在实验报告中进行了详细说明，更多说明见实验报告。
