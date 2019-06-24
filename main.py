import itchat
import matplotlib.pyplot as plt

itchat.auto_login(hotReload=False)
itchat.dump_login_status()

we_friend = itchat.get_friends(update=True)[:]

total = len(we_friend[1:])
man = woman = other = 0
for fri_info in we_friend[1:]:
    # print('fri_info:', fri_info)
    sex = fri_info['Sex'] # 如果sex=1 代表男性 sex=2代表女性
    if sex == 1:
        man += 1
    elif sex == 2:
        woman += 1
    else:
        other += 1

man_ratio = int(man)/total * 100  # 用来正常显示中文标签plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号plt.figure(figsize=(5, 5))  # 绘制的图片为正圆sex_li = ['男', '女', '其他']radius = [0.01, 0.01, 0.01]  # 设定各项距离圆心n个半径colors = ['red', 'yellowgreen', 'lightskyblue']proportion = [man_ratio, woman_ratio, other_ratio]plt.pie(proportion, explode=radius, labels=sex_li, colors=colors, autopct='%.2f%%')   # 绘制饼图# 加入图例 loc =  'upper right' 位于右上角 bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边 borderaxespad = 0.3图例的内边距plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.1), borderaxespad=0.3)# 绘制标题plt.title('微信好友性别比例')    # 展示plt.show()100
woman_ratio = int(woman)/total * 100
other_ratio = int(other)/total * 100

plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(5, 5))  # 绘制的图片为正圆
sex_li = ['男', '女', '其他']
radius = [0.01, 0.01, 0.01]  # 设定各项距离圆心n个半径
colors = ['red', 'yellowgreen', 'lightskyblue']
proportion = [man_ratio, woman_ratio, other_ratio]

plt.pie(proportion, explode=radius, labels=sex_li, colors=colors, autopct='%.2f%%')   # 绘制饼图

# 加入图例 loc =  'upper right' 位于右上角 bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边 borderaxespad = 0.3图例的内边距
plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.1), borderaxespad=0.3)

# 绘制标题
plt.title('微信好友性别比例')

# 展示
plt.show()

import os
import math
import numpy as np
from PIL import Image
num = 0
pwd_path = os.path.abspath(os.path.dirname(os.getcwd()))
print("pwd_path:", pwd_path)
"""
desc_photos = os.path.join(pwd_path,  'weChat\photos')
if  not os.path.exists(desc_photos):
    os.makedirs(desc_photos)
for  i  in  we_friend:
        img  =  itchat.get_head_img(userName=i["UserName"])
        # print(np.array(img).shape, i)
        file_image  =  open(desc_photos + "\%s.jpg"%str(num),  'wb')
        file_image.write(img)
        file_image.close()
        num  +=  1

ls = os.listdir(desc_photos)
each_size  =  int(math.sqrt(float(640  *  640)  /  len(ls)))    #  算出每张图片的大小多少合适
lines  =  int(640  /  each_size)
image  =  Image.new('RGBA',  (640,  640))      #  创建640*640px的大图
x  =  0
y  =  0
j = 0
for  i  in  range(0,  len(ls)  +  1):
        try:
            print(desc_photos  + "\%s.jpg"%str(i))
            img  =  Image.open(desc_photos  + "\%s.jpg"%str(i))
        except  IOError:
            print("Error", j)
            j+=1
        else:
            img  =  img.resize((each_size,  each_size),  Image.ANTIALIAS)
            image.paste(img,  (x  *  each_size,  y  *  each_size))        #  粘贴位置
            x  +=  1
            if  x  ==  lines:    #  换行
                    x  =  0
                    y  +=  1

image.save("./好友头像拼接图.png")

prov_dict,  city_dict  =  {},  {}
for  fri_info  in  we_friend[1:]:
    prov  =  fri_info['Province']
    city  =  fri_info['City']
    if  prov  and  prov  not  in  prov_dict.keys():
            prov_dict[prov]  =  1
    elif  prov:
            prov_dict[prov]  +=  1
    if  city  and  city  not  in  city_dict.keys():
            city_dict[city]  =  1
    elif  city:
            city_dict[city]  +=  1

#  区域Top10
prov_dict_top10  =  sorted(prov_dict.items(),  key=lambda  x:  x[1],  reverse=True)[0:10]
#  城市Top10
city_dict_top10  =  sorted(city_dict.items(),  key=lambda  y:  y[1],  reverse=True)[0:10]

prov_nm,  prov_num  =  [],  []    #  省会名  +  数量
for  prov_data  in  prov_dict_top10:
    prov_nm.append(prov_data[0])
    prov_num.append(prov_data[1])

pwd_path  =  os.path.abspath(os.path.dirname(os.getcwd()))
desc_full  =  os.path.join(pwd_path,  'weChat/photos')
if  not os.path.exists(desc_full):
    os.makedirs(desc_full)
colors  =  ['#00FFFF',  '#7FFFD4',  '#F08080',  '#90EE90',  '#AFEEEE',
                    '#98FB98',  '#B0E0E6',  '#00FF7F',  '#FFFF00',  '#9ACD32']
plt.rcParams['font.sans-serif']  =  ['SimHei']    #  用来正常显示中文标签
plt.rcParams['axes.unicode_minus']  =  False    #  用来正常显示负号

index  =  range(len(prov_num))
plt.bar(index,  prov_num,  color=colors,  width=0.5,  align='center')

plt.xticks(range(len(prov_nm)),  prov_nm)    #  横坐轴标签
for  x,  y  in  enumerate(prov_num):
        #  在柱子上方1.2处标注值
        plt.text(x,  y  +  1.2,  '%s'  %  y,  ha='center',  fontsize=10)
plt.ylabel('省会好友人数')    #  设置纵坐标标签
prov_title  =  '微信好友区域Top10'
plt.title(prov_title)        #  设置标题
plt.savefig(desc_full  +  '/微信好友区域Top10')    #  保存图片
"""

import re
import os
import jieba
from snownlp import SnowNLP

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
sign_li = []
rule = re.compile("1fd+w*|[<>/=]")    # 定义正则规则
for fri_info in we_friend[1:]:
    signature = fri_info['Signature']
    if signature:
        sign_deal = signature.replace(' ', '').replace('	', '').replace(' ', '').replace("span", "").replace("class", "").replace("emoji", "")
        sign = rule.sub("", sign_deal)
        sign_li.append(sign)

pwd_path = os.path.abspath(os.path.dirname(os.getcwd()))
conf_path = os.path.join(pwd_path, 'weChat/conf/')
if  not os.path.exists(conf_path):
    os.makedirs(conf_path)
comment_txt = ''
back_img = plt.imread(conf_path + '/peiqi.png')  ####背景图  生成中文词表的背景图
cloud = WordCloud(font_path=conf_path + '/simhei.ttf',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
                  background_color="white",  # 背景颜色
                  max_words=5000,  # 词云显示的最大词数
                  mask=back_img,  # 设置背景图片
                  max_font_size=100,  # 字体最大值
                  random_state=42,
                  width=360, height=591, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,保存的图片大小将会按照其大小保存,margin为词语边缘距离
                  )
for li in sign_li:
    comment_txt += ' '.join(jieba.cut(li, cut_all=False))
wc = cloud.generate(comment_txt)
image_colors = ImageColorGenerator(back_img)
plt.figure("wordc")
plt.imshow(wc.recolor(color_func=image_colors))
wc.to_file('./好友个性签名词云图.png')

sentimentslist = []
for li in sign_li:
    if len(li) > 0:
        s = SnowNLP(li)
        print(li, s.sentiments)
        sentimentslist.append(s.sentiments)
fig1 = plt.figure("sentiment")
plt.hist(sentimentslist, bins=np.arange(0, 1, 0.02))
plt.savefig('./好友签名情感分析')
plt.show()
