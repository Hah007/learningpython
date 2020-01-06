from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt
from skimage.io import imread

text = open('.\\庆余年-CODE\\qingyunian.txt', 'r').read()  # 读取一个TXT文件
bg_pic = imread('.\\庆余年-CODE\\beijing.png')
'''设置词云样式'''
wc = WordCloud(
    background_color='white',
    mask=bg_pic,
    font_path='simhei.ttf',
    max_words=2000,
    max_font_size=150,
    random_state=30,
    scale=1.5
)

wc.generate_from_text(text)
image_colors=ImageColorGenerator(bg_pic)
plt.imshow(wc)
plt.axis('off')
plt.show()
print('display success!')
wc.to_file('test.jpg')
