#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 激活函数对比图.py
# @Author: WangYe
# @Date  : 2020/3/19
# @Software: PyCharm

from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei']
y1=[1194,1096,996,806,756,622,504,659,714,801,898]
x1=[1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3]
# x3=[4,6,8,10,15,20]#单机代码
x2=[1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3]
y2=[1194,1194,1194,1194,1194,1194,1194,1194,1194,1194,1194]

# y3=[1799,1799,1799,1799,1799,1799]
# plt.plot(y1)
plt.plot(x1,y1,label='改进方法',linewidth=3,
         color='black',
         marker='*',
markerfacecolor='black',
         markersize=10)
plt.plot(x2,y2,linewidth=3,
         label = '传统方法'
         , color='black'
         # ,marker='v',
,markerfacecolor='black',markersize=12
         )
# plt.plot(x2,y2,label='SSGD')
# plt.plot(x3,y3,label='Single')
# plt.xlabel('m')
# plt.ylabel('costing time')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('α',size = 20)
plt.ylabel('time(s)',size = 20)
plt.title('实验2中α参数对耗时的影响',size=20)
plt.legend()
plt.savefig('CNN.svg',format = 'svg')
# plt.savefig('our3.png')
plt.show()
