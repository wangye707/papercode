#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 扇形统计图.py
# @Author: WangYe
# @Date  : 2020/3/17
# @Software: PyCharm
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# color[img == 0] = [255, 255, 255]  # 其他，白色，0  765
# color[img == 1] = [0, 255, 0]  # 植被，绿色，1    255
# color[img == 2] = [0, 0, 0]  # 道路，黑色，2    0
# color[img == 3] = [131, 139, 139]  # 建筑，黄色，3   409
# color[img == 4] = [19, 69, 139]  # 水体，蓝色，4    227
from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 设置绘图的主题风格（不妨使用R中的ggplot分隔）
plt.style.use('ggplot')

# 构造数据
#{255: 1518160, 765: 10528901, 409: 6400746, 0: 2057708, 227: 25897}
#print('植被（标记1）、道路（标记2）、建筑（标记3）、水体（标记4）以及其他(标记0)')
edu = [10528901, 1518160, 2057708, 6400746,25897]
labels = ['背景', '植被', '道路','建筑','水体']
explode = [0, 0, 0, 0, 0.1]  # 用于突出显示大专学历人群
colors = ['white', 'GREEN', 'BLACK', 'GRAY', 'BLUE']  # 自定义颜色
# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0, 4)
plt.ylim(0, 4)

# 绘制饼图
plt.pie(x=edu,  # 绘图数据
        explode=explode,  # 突出显示大专人群
        labels=labels,  # 添加教育水平标签
        colors=colors,  # 设置饼图的自定义填充色
        autopct='%.2f%%',  # 设置百分比的格式，这里保留一位小数
        pctdistance=0.8,  # 设置百分比标签与圆心的距离
        labeldistance=1.4,  # 设置教育水平标签与圆心的距离
        startangle=180,  # 设置饼图的初始角度
        radius=1,  # 设置饼图的半径
        counterclock=False,  # 是否逆时针，这里设置为顺时针方向
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'black'},  # 设置饼图内外边界的属性值
        textprops={'fontsize': 14, 'color': 'red'},  # 设置文本标签的属性值
        center=(1.8, 1.8),  # 设置饼图的原点
        frame=1)  # 是否显示饼图的图框，这里设置显示

# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())
# 添加图标题
plt.title('航拍图片百分比统计')

# 显示图形
plt.show()