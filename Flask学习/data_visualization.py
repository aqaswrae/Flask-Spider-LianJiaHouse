import os
import json
from pyecharts.charts import Bar, Line, Pie
from pyecharts.options import TitleOpts, ToolboxOpts, VisualMapOpts, LabelOpts, AxisOpts, LegendOpts, GraphicGroup,GraphicItem

# VisualMapOpts：视觉映射组件
# LegendOpts：配置图例组件的选项对象
# GraphicGroup（图形组）提供了一个批量操作视觉元素的容器
# GraphicItem（图形元素）是由 Graphic 对象组成的一种可视化元素
'''
小区名称-均价图
小区名称-总价图
各地区-房产数量图--可以用柱状图，也可以用饼图
开发商建造小区数量图--可以用柱状图，也可以用饼图
年份--建造小区数量图
'''

output_path = os.path.join(os.getcwd(), "templates")
#利用os模块创建一个路径变量output_path，该变量将当前工作目录（通过os.getcwd()获取）与一个名为"templates"的文件夹路径连接在一起

# ------------------------------------------------新房-------------------------------------------------------------------
# 读取新房json文件中的数据
# with open('','r',encoding='utf-8') as f_new:
#     newhouse_lst = json.load(f_new)
# 地区的数据
# new_location_data = []
# 面积的数据
# new_area_data = []
# 均价的数据
# new_avgprice_data = []
# 总价的数据
# new_totalprice_data = []
# for i in newhouse_lst:
#     new_area = float(i['area'])
#     new_loc = i['location']
#     new_avg = int(i['avgprice'])
#     new_total = float(i['totalprice'])
#     new_location_data.append(new_loc)
#     new_avgprice_data.append(new_avg)
#     new_totalprice_data.append(new_total)


# ------------------------------------------------二手房-----------------------------------------------------------------
# 读取二手房json文件中的数据
with open('dataspider/oldhousedata.json', 'r', encoding='utf-8') as f_old:
    oldhouse_lst = json.load(f_old)
# 小区名称的数据
old_housename_data = []
# 年份的数据
old_year_data = []
# 地区的数据
old_location_data = []
# 面积的数据
old_area_data = []
# 均价的数据
old_avgprice_data = []
# 总价的数据
old_totalprice_data = []
# 统计各地区房产数量的
licang_count = 0
jiaozhou_count = 0
laoshan_count = 0
chengyang_count = 0
shibei_count = 0
shinan_count = 0
huangdao_count = 0
jimo_count = 0
for i in oldhouse_lst:
    old_housename = i['housename']
    old_year = i['year']
    old_area = float(i['area'])
    old_loc = i['location']
    old_avg = int(i['avgprice'])
    old_total = float(i['totalprice'])
    old_housename_data.append(old_housename)
    old_year_data.append(old_year)
    old_location_data.append(old_loc)
    old_avgprice_data.append(old_avg)
    old_totalprice_data.append(old_total)

for i in oldhouse_lst:
    if i['location'] == '李沧':
        licang_count = licang_count + 1
    elif i['location'] == '胶州':
        jiaozhou_count = jiaozhou_count + 1
    elif i['location'] == '崂山':
        laoshan_count = laoshan_count + 1
    elif i['location'] == '城阳':
        chengyang_count = chengyang_count + 1
    elif i['location'] == '市北':
        shibei_count = shibei_count + 1
    elif i['location'] == '市南':
        shinan_count = shinan_count + 1
    elif i['location'] == '黄岛':
        huangdao_count = huangdao_count + 1
    elif i['location'] == '即墨':
        jimo_count = jimo_count + 1

# print(old_housename_data)
# print(old_location_data)
# print(old_avgprice_data)
# print(old_totalprice_data)

line1 = Line()

# 1.小区名称-均价图--柱状图
pie2 = Pie()
def generate_chart1():
    pie2.add('均价',[(i,j)for i,j in zip(old_housename_data,old_avgprice_data)])
    pie2.set_global_opts(
        title_opts=TitleOpts(title='小区名称-均价关系饼图'),
        legend_opts=LegendOpts(pos_right="right"),  # 设置图例位置
        # 设置饼图位置和大小
        graphic_opts=GraphicGroup(graphic_item=GraphicItem(left="center", top="20%", width="60%"))
    )
    pie2.render(os.path.join(output_path, '二手房(小区名称-均价图).html'))

# 2.小区名称-总价图--要不用饼图吧
pie1 = Pie()
def generate_chart2():
    pie1.add('总价', [(i, j) for i, j in zip(old_housename_data, old_totalprice_data)])
    pie1.set_global_opts(
        title_opts=TitleOpts(title='小区名称-总价关系饼图'),
        legend_opts=LegendOpts(pos_right="right"),  # 设置图例位置
        # 设置饼图位置和大小
        graphic_opts=GraphicGroup(graphic_item=GraphicItem(left="center", top="20%", width="60%"))
    )
    pie1.render(os.path.join(output_path, '二手房(小区名称-总价图).html'))

# 3.各地区-房产数量图--可以用柱状图，也可以用饼图
# pie1 = Pie()
bar2 = Bar()
def generate_chart3():
    bar2.add_xaxis(['崂山', '胶州', '李沧', '即墨', '市南', '市北', '黄岛', '城阳'])
    bar2.add_yaxis('房产数量',
                   [laoshan_count, jiaozhou_count, licang_count, jimo_count, shinan_count, shibei_count, huangdao_count,
                    chengyang_count])
    bar2.set_global_opts(
        title_opts=TitleOpts(title='各地区-房产数量柱状图'),
        toolbox_opts=ToolboxOpts(is_show=True),
        visualmap_opts=VisualMapOpts(is_show=True)
    )
    bar2.render(os.path.join(output_path, '二手房(各地区-房产数量图).html'))


# 4.开发商建造小区数量图--可以用柱状图，也可以用饼图---需要新房产数据解决
def geerate_chart4():
    print(list(set()))


# 5.年份--建造小区数量图
x_year = ['1931年建成', '1945年建成', '1946年建成', '1974年建成', '1977年建成', '1978年建成', '1979年建成', '1980年建成', '1982年建成',
          '1983年建成', '1984年建成', '1985年建成', '1986年建成', '1987年建成', '1988年建成', '1989年建成', '1990年建成', '1991年建成',
          '1992年建成', '1993年建成', '1994年建成', '1995年建成', '1996年建成', '1998年建成', '1999年建成', '2000年建成', '2001年建成',
          '2002年建成', '2003年建成', '2004年建成', '2006年建成', '2007年建成', '2008年建成', '2009年建成', '2010年建成', '2011年建成',
          '2012年建成', '2013年建成', '2014年建成', '2015年建成', '2016年建成', '2017年建成', '2018年建成', '2019年建成', '2020年建成',
          '2021年建成']
y_1931, y_1945, y_1946, y_1974, y_1977, y_1978, y_1979, y_1980, y_1982, y_1983, y_1984, y_1985, y_1986, y_1987, y_1988 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
y_1989, y_1990, y_1991, y_1992, y_1993, y_1994, y_1995, y_1996, y_1998, y_1999, y_2000, y_2001, y_2002, y_2003, y_2004 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
y_2006, y_2007, y_2008, y_2009, y_2010, y_2011, y_2012, y_2013, y_2014, y_2015, y_2016, y_2017, y_2018, y_2019, y_2020, y_2021 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for i in oldhouse_lst:
    if i['year'] == '1931年建成 ':y_1931 = y_1931 + 1
    elif i['year'] == '1945年建成 ':y_1945 = y_1945 + 1
    elif i['year'] == '1946年建成 ':y_1946 = y_1946 + 1
    elif i['year'] == '1974年建成 ':y_1974 = y_1974 + 1
    elif i['year'] == '1977年建成 ':y_1977 = y_1977 + 1
    elif i['year'] == '1978年建成 ':y_1978 = y_1978 + 1
    elif i['year'] == '1979年建成 ':y_1979 = y_1979 + 1
    elif i['year'] == '1982年建成 ':y_1982 = y_1982 + 1
    elif i['year'] == '1983年建成 ':y_1983 = y_1983 + 1
    elif i['year'] == '1984年建成 ':y_1984 = y_1984 + 1
    elif i['year'] == '1985年建成 ':y_1985 = y_1985 + 1
    elif i['year'] == '1986年建成 ':y_1986 = y_1986 + 1
    elif i['year'] == '1987年建成 ':y_1987 = y_1987 + 1
    elif i['year'] == '1988年建成 ':y_1988 = y_1988 + 1
    elif i['year'] == '1989年建成 ':y_1989 = y_1989 + 1
    elif i['year'] == '1990年建成 ':y_1990 = y_1990 + 1
    elif i['year'] == '1991年建成 ':y_1991 = y_1991 + 1
    elif i['year'] == '1992年建成 ':y_1992 = y_1992 + 1
    elif i['year'] == '1993年建成 ':y_1993 = y_1993 + 1
    elif i['year'] == '1994年建成 ':y_1994 = y_1994 + 1
    elif i['year'] == '1995年建成 ':y_1995 = y_1995 + 1
    elif i['year'] == '1996年建成 ':y_1996 = y_1996 + 1
    elif i['year'] == '1998年建成 ':y_1998 = y_1998 + 1
    elif i['year'] == '1999年建成 ':y_1999 = y_1999 + 1
    elif i['year'] == '2000年建成 ':y_2000 = y_2000 + 1
    elif i['year'] == '2001年建成 ':y_2001 = y_2001 + 1
    elif i['year'] == '2002年建成 ':y_2002 = y_2002 + 1
    elif i['year'] == '2003年建成 ':y_2003 = y_2003 + 1
    elif i['year'] == '2004年建成 ':y_2004 = y_2004 + 1
    elif i['year'] == '2006年建成 ':y_2006 = y_2006 + 1
    elif i['year'] == '2007年建成 ':y_2007 = y_2007 + 1
    elif i['year'] == '2008年建成 ':y_2008 = y_2008 + 1
    elif i['year'] == '2009年建成 ':y_2009 = y_2009 + 1
    elif i['year'] == '2010年建成 ':y_2010 = y_2010 + 1
    elif i['year'] == '2011年建成 ':y_2011 = y_2011 + 1
    elif i['year'] == '2012年建成 ':y_2012 = y_2012 + 1
    elif i['year'] == '2013年建成 ':y_2013 = y_2013 + 1
    elif i['year'] == '2014年建成 ':y_2014 = y_2014 + 1
    elif i['year'] == '2015年建成 ':y_2015 = y_2015 + 1
    elif i['year'] == '2016年建成 ':y_2016 = y_2016 + 1
    elif i['year'] == '2017年建成 ':y_2017 = y_2017 + 1
    elif i['year'] == '2018年建成 ':y_2018 = y_2018 + 1
    elif i['year'] == '2019年建成 ':y_2019 = y_2019 + 1
    elif i['year'] == '2020年建成 ':y_2020 = y_2020 + 1
    elif i['year'] == '2021年建成 ':y_2021 = y_2021 + 1

bar3 = Bar()


def generate_chart5():
    # print(list(set(old_year_data)))
    # print(len(list(set(old_year_data))))
    bar3.add_xaxis(x_year)
    bar3.add_yaxis('', [y_1931, y_1945, y_1946, y_1974, y_1977, y_1978, y_1979, y_1980, y_1982, y_1983, y_1984, y_1985,
                        y_1986, y_1987, y_1988, y_1989, y_1990, y_1991, y_1992, y_1993, y_1994, y_1995, y_1996, y_1998,
                        y_1999, y_2000, y_2001, y_2002, y_2003, y_2004, y_2006, y_2007, y_2008, y_2009, y_2010, y_2011,
                        y_2012, y_2013, y_2014, y_2015, y_2016, y_2017, y_2018, y_2019, y_2020, y_2021])
    bar3.render(os.path.join(output_path, '二手房(年份--建造小区数量图).html'))


# bar = Bar()
#
#
# bar.add_xaxis(list(set(old_location_data)))
# bar.add_yaxis('均价',[sum(old_avgprice_data[i] for i in range(len(old_location_data))if old_location_data[i]==item) for item in set(old_location_data)])
# bar.render('均价可视图.html')
# print(os.getcwd())
# 当你需要将 x 轴上相同的城市累加到一个值上并且回显到 y 轴上时，可以使用下面的一行代码来达到目的：
# ```python
# [sum([y_data[i] for i in range(len(x_data)) if x_data[i]==item]) for item in set(x_data)]
# ```
# 这段代码使用了一个列表推导式来完成操作，您可以尝试拆分开来，逐个理解其构成部分和运行逻辑。详细解释如下：
# 1. 首先得到 x 轴上不重复的城市名列表，使用 `set(x_data)` 来去重。
# 2. 使用列表推导式构造一个新的列表，其中 item 来自于 x 轴上的不重复的城市名列表，表示当前需要对哪个城市的数据进行累加求和：
#    ```python
#    [ ... for item in set(x_data)]
#    ```
# 3. 对于每个城市名 item，在 x 轴数据列表 x_data 中找到所有值相等的位置下标 i，使用列表推导式构造一个包含下标 i 的列表：
#    ```python
#    [i for i in range(len(x_data)) if x_data[i]==item]
#    ```
# 4. 对于构造好的下标列表，使用列表推导式将 y 轴上的值进行累加求和：
#    ```python
#    sum([y_data[i] for i in range(len(x_data)) if x_data[i]==item])
#    ```
# 5. 将求和的结果作为列表推导式的当前元素，最终得到对应城市在 y 轴上的数据列表。
# 完整的代码如下：
# ```python
# [sum([y_data[i] for i in range(len(x_data)) if x_data[i]==item]) for item in set(x_data)]
# ```
# 这段代码可以理解成 x 轴上每个城市的累加值构成了一个新的列表，其中列表中元素的排列顺序和 set(x_data) 中的顺序完全相同。为了更好地理解这段代码的执行逻辑，你可以尝试将其拆解为多个步骤，逐个调试和修改其中的参数，直到你完全理解其内部实现的逻辑。

if __name__ == '__main__':
    generate_chart1()
    generate_chart2()
    generate_chart3()
    generate_chart5()
    # print([y_1931,y_1979,y_1986,y_1992,y_1999,y_2006,y_2012,y_2018])
