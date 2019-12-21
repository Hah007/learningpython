# # 引入requests库
# import requests

# # 发出请求，并把返回的结果放在变量res中
# res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# # 把Reponse对象的内容以二进制数据的形式返回
# pic = res.content
# # 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# # 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
# photo = open('ppt.jpg','wb')
# # 获取pic的二进制内容
# photo.write(pic) 
# # 关闭文件
# photo.close()

import requests
#引用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
# res.encoding='utf-8'
#定义Reponse对象的编码为utf-8。
novel=res.text
#把Response对象的内容以字符串的形式返回
print(novel[:800])
#打印小说的前800个字。