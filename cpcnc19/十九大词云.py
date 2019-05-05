#author:WeiminLee
#-*-coding:utf-8-*-
#date:''
#function=''
import jieba
with open('report19.txt') as f:
    s = f.read()
print len(s)
cut = jieba.cut(s,cut_all=False)
cut1 = list(cut)
from collections import Counter

num = Counter(cut1)
nummost = num.most_common(128)
mydict = {}
for word in nummost:
    if word[0]  in [u"，",u"。",u"、",u"和",u"的",u" ",u"（",u"）",u"“",u"”",u"为",u"；",u"!"]:
        pass
    elif len(word[0])==1:
        pass
    else:
        mydict[word[0]] = word[1]
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
bgpicture = imread('D:\Documents\Desktop\Web\snippet-master\snippet-master\cpcnc19\picture40.jpg')
wc = WordCloud(font_path='zhaozi.ttf', background_color='black',mask=bgpicture,max_font_size=100)
wc.generate_from_frequencies(mydict)
image_colors = ImageColorGenerator(bgpicture)
wc.recolor(color_func=image_colors)

import matplotlib.pyplot as plt
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show(wc)
wc.to_file('wangzherongyao.jpg')