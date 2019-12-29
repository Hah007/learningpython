# import csv
# with open('test.csv','a', newline='',encoding='utf-8') as f:
#     writer  = csv.writer(f)
#     writer.writerow(['4', '猫砂', '25', '1022', '886'])
#     writer.writerow(['5', '猫罐头', '18', '2234', '3121'])



import csv
#引用csv模块。

# data = [['wufeng ', 'wufeng@qq.com'],['kaxi', 'kaxi@qq.com']]
# #待写入csv文件的内容

# with open('to_addrs.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     for row in data:
#         writer.writerow(row)


import csv
#引用csv模块。
to_addrs=[]

with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader)
    for row in reader: 
        #print(row)
        to_addrs.append(row[1])
print(to_addrs)