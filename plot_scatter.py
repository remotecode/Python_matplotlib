# -*- coding: utf-8 -*-
#画多条折线图
import numpy             as     np
import matplotlib.pyplot as     plt
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/year.xlsx')#open file
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
date     = sheet.col_values(0)#[0:365]#表示取第0-第365行
IMS      = sheet.col_values(1)#[0:365] #col = sheet.col_values(0)##获取第一列的数据
MOD_SSMI = sheet.col_values(2)#[0:365] #row = sheet.row_values(0)##获取第一行的数据
MOD_B    = sheet.col_values(3)#[0:365]
TAI      = sheet.col_values(4)#[0:365]
I_TAI    = sheet.col_values(5)#[0:365]
average  = sheet.col_values(6)#[0:365]
####################################
fig   = plt.figure(figsize=(13,5))#设置图形界面的大小
ax    = fig.add_subplot(111)
# ax.scatter(date,IMS,     marker='H', color='b', s=20)
# ax.scatter(date,MOD_SSMI,marker='H', color='c', s=20)
# ax.scatter(date,MOD_B,   marker='H', color='k', s=20)
# ax.scatter(date,TAI,     marker='H', color='g', s=20)
# ax.scatter(date,I_TAI,   marker='H', color='y', s=20)
# ax.scatter(date,average, marker='H', color='r', s=20)
######################################
ax.plot(date,IMS,     'b-o', label='IMS',     linewidth=2)
ax.plot(date,MOD_SSMI,'c-D', label='MOD-SSMI',linewidth=2,linestyle='--')
ax.plot(date,MOD_B,   'k-h', label='MOD-B',   linewidth=2)
ax.plot(date,TAI,     'g-v', label='TAI',     linewidth=2,linestyle='--')
ax.plot(date,I_TAI,   'm-p', label='I-TAI',   linewidth=2)
ax.plot(date,average, 'r-s', label='Average', linewidth=2)
######################################
ax.set_ylim(300000,1200000)#Y轴的数值范围
ax = plt.gca()  # 获取当前图像的坐标轴信息
ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。
######################################
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)
plt.legend(loc='upper right')#图例
plt.grid(True,axis='y')#设置网格线
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_xticklabels(['2004-2005','2005-2006','2006-2007',\
	'2007-2008','2008-2009','2009-2010',\
	'2010-2011','2011-2012','2012-2013','2013-2014']) 
fig.autofmt_xdate()#旋转X轴标签
# ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
ax.set_xlabel('Hydrological years',fontproperties=font)
ax.set_ylabel('Snow Cover Area$(km^2)$',fontproperties=font)
##############################################
# plt.legend(numpoints=1)
plt.legend(loc='upper center',numpoints=1,bbox_to_anchor=(0.74,1.00),ncol=3,fancybox=True,shadow=True)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext,fontproperties=font)
# batt.plot()
plt.show()
fig.savefig('sample.png',dpi=900)
print 'end'