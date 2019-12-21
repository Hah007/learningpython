print('请输入两个数字(用，分割)：')
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
print(dimensions)
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
 
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
 
for i in range(rowNum):
    print (multilist[i])
