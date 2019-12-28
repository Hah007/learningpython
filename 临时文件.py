# 这个图片说明：?category=NCEE 这一个XHR，访问了网址https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=NCEE

# 在此，“NCEE”出现了两次：这个XHR的名字里面有“NCEE”，它访问的网址里面也有“NCEE”。

# 这就揭示了一种对应关系：当我们选择“高考”词库，那么下一个XHR，访问的网址就会是用“NCEE”来结尾。

# 可以多试几个词库验证下我们的猜测，的确里面的对应关系是一致的。考研和NGEE一组，四级和CET4一组，六级和CET6一组。

# 第1个XHR，所访问的网址规律就是：'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+'你选择的词库，对应的代码'。
# 如图，它下载到的是一个字典。字典里，包含了用来测试词汇量的50个单词。
# 第0，它先给出单词。
# 第1，它给出四个不同的翻译，每个翻译都有一个对应的pk值和rank值。
# 第2，它再给出一组pk值和rank值。它们，和正确翻译里面的pk值与rank值一致。
list=['CET4','CET6','NCEE','NGEE']
print(list[1])

list1=[]
list2=[]
chioce=0
for i  in  range(50):
    chioce=int(input('你是否认识这个单词（1是，2否）'+'\n'))

    if chioce==1:
        list1.append(i)
    else:
        list2.append(i)