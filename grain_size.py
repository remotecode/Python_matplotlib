# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/grain_size.xlsx')
# read seperate data
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
observation = sheet.col_values(2)[1:40]#表示取第0-第365行
ww_data     = sheet.col_values(4)[1:40]
#########################################
fig         = plt.figure(figsize=(6,5))#设置图形界面的大小
ax          = fig.add_subplot(111)
#########################################
plt.scatter(observation, ww_data, marker='o', color='b', s=80)
lx1=np.linspace(-10,10,5)
ly1=lx1
plt.plot(lx1,ly1,linewidth=1.0,color='r')
plt.xlim(0.5,1)
plt.ylim(0.5,1)
#########################################
xmajorLocator   = MultipleLocator(0.05) #将x主刻度标签设置为20的倍数
xminorLocator   = MultipleLocator(0.05) #将x轴次刻度标签设置为5的倍数
ymajorLocator   = MultipleLocator(0.05) #将y主刻度标签设置为20的倍数
yminorLocator   = MultipleLocator(0.05) #将y轴次刻度标签设置为5的倍数
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)
#显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)

font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
#########################################
plt.xlabel('Yakou Snow Albedo',fontproperties=font)
plt.ylabel('TARTES Snow Albedo',   fontproperties=font)
##############################################
plt.legend()
# batt.plot()
plt.show()
fig.savefig('snow grain size.png',dpi=900)
print 'end'