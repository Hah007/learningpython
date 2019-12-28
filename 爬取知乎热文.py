import requests
import csv

csv_file=open('zhihudongjing.csv','w',newline='',encoding='utf-8')
writer=csv.writer(csv_file)
list2=['标题','链接','摘要']
writer.writerow(list2)
#调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “标题”和“链接”和"摘要"。

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#封装headers
#url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
url='https://www.zhihu.com/api/v4/members/rosiel-chen/articles?'
articlelist=[]
#空列表，等待数据
offset=0
#设置起始值为0
while True:
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':'10',
        'limit':'20',
        'sort_by':'voteups',
        }
    #封装参数
    res=requests.get(url,headers=headers,params=params)
    #发送请求，并把响应内容赋值到变量res里面
    print(res.status_code)
    #确认请求成功  
    articles=res.json()
    #用json()方法去解析response对象，并赋值到变量articles上面。
    #print(articles)
    #打印这个json文件
    data=articles['data']
    #取出键为data的值。
    for i in data:
        list1=[i['title'],i['url'],i['excerpt']]
        #articlelist.append(list1)
        #遍历列表，拿到的是列表里的每一个元素，这些元素都是字典，再通过键把值取出来
        writer.writerow(list1)
        
    offset+=20
    if offset>40:
        break
    # 如果键is_end所对应的值是True，就结束while循环。
        #if articles['paging']['is_end'] == True:
            #break
        # ————————————————————————————————————
#print(articlelist)
csv_file.close()
print('爬取完毕')
