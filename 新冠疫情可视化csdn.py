# -*- coding: utf-8 -*-

import time
import json
import requests
from datetime import datetime
import numpy as np
import matplotlib
import matplotlib.figure
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.rcParams['font.sans-serif'] = ['FangSong']  # 设置默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时'-'显示为方块的问题

def catch_daily():
    """抓取每日确诊和死亡数据"""

    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()*1000)
    data = json.loads(requests.get(url=url).json()['data'])
    data.sort(key=lambda x:x['date'])

    date_list = list() # 日期
    confirm_list = list() # 确诊
    suspect_list = list() # 疑似
    dead_list = list() # 死亡
    heal_list = list() # 治愈
    for item in data:
        # print(item)
        month, day = item['date'].split('/')
        date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))

    return date_list, confirm_list, suspect_list, dead_list, heal_list

def catch_distribution():
    """抓取行政区域确诊分布数据"""

    data = {'西藏':0}
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=%d'%int(time.time()*1000)
    for item in json.loads(requests.get(url=url).json()['data']):
        if item['area'] not in data:
            data.update({item['area']:0})
        data[item['area']] += int(item['confirm'])

    return data

def plot_daily():
    """绘制每日确诊和死亡数据"""

    # date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily() # 获取数据
 # 获取每日疫情数据，日期，确诊，疑似，死亡，治愈
    date_list, everyday_confirm, everyday_suspect, everyday_dead, everyday_heal = catch_daily()

    # 显示中文和显示负号
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 绘制画布和子图对象
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # 左Y轴绘制确诊和疑似病例曲线
    ax1.plot(date_list, everyday_confirm, lw=2, ls='--', marker='o', color='red', label='确诊')
    ax1.plot(date_list, everyday_suspect, lw=2, ls='--', marker='o', color='orange', label='疑似')
    # 设置标题，XY轴标题，刻度
    ax1.set_title("2019-nCoV疫情变化时间图", fontsize=16)
    ax1.set_xlabel("2020年1月", fontsize=16)
    ax1.set_xticklabels(date_list, rotation=30)
    ax1.set_ylabel(r"确诊及疑似人数", fontsize=16)
    ax1.set_ylim(0, 16000)
    # 显示网格线和显示图例
    plt.grid(which='major', axis='both', color='grey', linestyle='--', alpha=0.2)
    plt.legend(loc='upper left', bbox_to_anchor=(0.3,1))

    # 右Y轴绘制死亡和治愈病例曲线,共用ax1的X轴
    ax2 = ax1.twinx()
    ax2.plot(date_list, everyday_dead, lw=1, ls='--', marker='.', color='cyan', label='死亡')
    ax2.plot(date_list, everyday_heal, lw=1, ls='--', marker='.', color='green', label='治愈')
    # 设置标题刻度
    ax2.set_ylabel(r"死亡及治愈人数", fontsize=16)
    ax2.set_ylim(0, 400)
    # 显示网格线和显示图例
    plt.grid(which='major', axis='both', color='grey', linestyle='--', alpha=0.2)
    plt.legend(loc='upper center')

    # 展示图形
    plt.show()
    # 保存图形为图片,第一个参数保存路径，第二个参数裁掉多余的空白部分
    plt.savefig('2019-nCoV疫情变化时间图.png', bbox_inches='tight')

    # plt.figure('2019-nCoV疫情统计图表', facecolor='#f4f4f4', figsize=(10, 8))
    # plt.title('2019-nCoV疫情曲线', fontsize=20)

    # plt.plot(date_list, confirm_list, label='确诊')
    # plt.plot(date_list, suspect_list, label='疑似')
    # plt.plot(date_list, dead_list, label='死亡')
    # plt.plot(date_list, heal_list, label='治愈')

    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # 格式化时间轴标注
    # plt.gcf().autofmt_xdate() # 优化标注（自动倾斜）
    # plt.grid(linestyle=':') # 显示网格
    # plt.legend(loc='best') # 显示图例
    # plt.savefig('2019-nCoV疫情曲线.png') # 保存为文件
    # plt.show()

def plot_distribution():
    """绘制行政区域确诊分布数据"""

    data = catch_distribution()

    font = FontProperties(fname='res/simsun.ttf', size=14)
    lat_min = 0
    lat_max = 60
    lon_min = 70
    lon_max = 140

    handles = [
            matplotlib.patches.Patch(color='#ffaa85', alpha=1, linewidth=0),
            matplotlib.patches.Patch(color='#ff7b69', alpha=1, linewidth=0),
            matplotlib.patches.Patch(color='#bf2121', alpha=1, linewidth=0),
            matplotlib.patches.Patch(color='#7f1818', alpha=1, linewidth=0),
]
    labels = [ '1-9人', '10-99人', '100-999人', '>1000人']

    fig = matplotlib.figure.Figure()
    fig.set_size_inches(10, 8) # 设置绘图板尺寸
    axes = fig.add_axes((0.1, 0.12, 0.8, 0.8)) # rect = l,b,w,h
    # m = Basemap(llcrnrlon=lon_min, urcrnrlon=lon_max, llcrnrlat=lat_min, urcrnrlat=lat_max, resolution='l', ax=axes)
    m = Basemap(projection='lcc', width=5000000, height=5000000, lat_0=36, lon_0=102, resolution='l', ax=axes)
    # m = Basemap(projection='ortho', lat_0=30, lon_0=105, resolution='l', ax=axes)
    m.readshapefile('res/china-shapefiles-master/china', 'province', drawbounds=True)
    m.readshapefile('res/china-shapefiles-master/china_nine_dotted_line', 'section', drawbounds=True)
    m.drawcoastlines(color='black') # 洲际线
    m.drawcountries(color='black')  # 国界线
    m.drawparallels(np.arange(lat_min,lat_max,10), labels=[1,0,0,0]) #画经度线
    m.drawmeridians(np.arange(lon_min,lon_max,10), labels=[0,0,0,1]) #画纬度线

    for info, shape in zip(m.province_info, m.province):
        pname = info['OWNER'].strip('\x00')
        fcname = info['FCNAME'].strip('\x00')
        if pname != fcname: # 不绘制海岛
            continue

        for key in data.keys():
            if key in pname:
                if data[key] == 0:
                    color = '#f0f0f0'
                elif data[key] < 10:
                    color = '#ffaa85'
                elif data[key] <100:
                    color = '#ff7b69'
                elif  data[key] < 1000:
                    color = '#bf2121'
                else:
                    color = '#7f1818'
                break

        poly = Polygon(shape, facecolor=color, edgecolor=color)
        axes.add_patch(poly)

    axes.legend(handles, labels, bbox_to_anchor=(0.5, -0.11), loc='lower center', ncol=4, prop=font)
    axes.set_title("2019-nCoV疫情地图", fontproperties=font)
    FigureCanvasAgg(fig)
    fig.show()
    fig.savefig('2019-nCoV疫情地图.png')

if __name__ == '__main__':
    plot_daily()
    plot_distribution()