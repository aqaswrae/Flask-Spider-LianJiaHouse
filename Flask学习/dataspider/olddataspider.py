import requests,json,time,datetime
from lxml import etree
# from app import app
from exts import db
from models import OldHouseModel
from werkzeug.utils import import_string



app = import_string('app.app')


headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
filepath = 'D:/Pycharm--professional/code/Flask学习/dataspider'


'''
housename = '//div[@class="positionInfo"]/a[1]/text()'第一层网址
year = '//div[@class="xiaoquInfo"]/div[1]/span[2]/text()'第二层名字链接
location = '//div[@class="areaName"]/span[@class="info"]/a[1]/text()'第二层网址图片链
room = '//div[@class="room"]/div[1]/text()'第二层网址图片链接
tag = '//div[@class="tag"]/span/text()'第一层网址
area = '//div[@class="area"]/div[1]/text()'第二层网址图片链接
avgprice = '//div[@class="unitPrice"]/span/text()'第二层网址图片链接
totalprice = '//span[@class="total"]/text()'第二层网址图片链接

nameHref = '//div[@class="positionInfo"]/a[1]/@href'
titleHref = '//div[@class="title"]/a/@href'
'''

class Data:
    @staticmethod
    def get_name(path,tree):
        housename = '//div[@class="positionInfo"]/a[1]/text()'
        substances = tree.xpath(path+housename)
        print(substances[0])
        return substances[0]
    @staticmethod
    def get_year(tree):
        year = '//div[@class="xiaoquInfo"]/div[1]/span[2]/text()'
        substances = tree.xpath(year)
        strr = ''
        if substances:
            print(substances[0])
            return substances[0]
        else:return strr
    @staticmethod
    def get_location(tree):
        location = '//div[@class="areaName"]/span[@class="info"]/a[1]/text()'
        substances = tree.xpath(location)
        print(substances[0])
        return substances[0]
    @staticmethod
    def get_room(tree):
        room = '//div[@class="room"]/div[1]/text()'
        substances = tree.xpath(room)
        strr = ''
        if substances:
            print(substances[0])
            return substances[0]
        else:return strr
    @staticmethod
    def get_tag(path,tree):
        tag = '//div[@class="tag"]/span/text()'
        substances = tree.xpath(path+tag)
        strr = ''
        if substances:
            for i in substances:
                strr += i
        print(strr)
        return strr
    @staticmethod
    def get_area(tree):
        area = '//div[@class="area"]/div[1]/text()'#要切片
        substances = tree.xpath(area)
        strr = ''
        if substances:
            print(substances[0][-3:])
            return substances[0].replace('平米','')
        else:return strr

    @staticmethod
    def get_avgPrice(tree):
        avgprice = '//div[@class="unitPrice"]/span/text()'
        substances = tree.xpath(avgprice)
        # print(substance[0].replace(',',''))
        strr = ''
        if substances:
            return substances[0]
        else:return strr
    @staticmethod
    def get_totalPrice(tree):
        totalprice = '//span[@class="total"]/text()'
        substances = tree.xpath(totalprice)
        strr = ''
        if substances:
            print(substances[0])
            return substances[0]
        else:return strr


#保存数据为json文件
def saveData(oldhousedata):
    with open(f'{filepath}/oldhousedata.json','w',encoding='utf-8') as f:
        json.dump(oldhousedata,f,ensure_ascii=False)

oldhousedata = []
baseUrl = 'https://qd.lianjia.com/ershoufang/pg'
def crawler():
    for page in range(22,23):
        print(f'============第{page}页============')
        url = baseUrl + str(page)
        content1 = requests.get(url,headers).text
        tree1 = etree.HTML(content1)
        for i in range(1,31):
            path1 = f'//ul[@class="sellListContent"]/li[{i}]'
            judge = tree1.xpath(path1)
            if judge:
                housename = Data.get_name(path1,tree1)
                tag = Data.get_tag(path1,tree1)
                path2 = f'//div[@class="positionInfo"]/a[1]/@href'
                nameHref = tree1.xpath(path1+path2)[0]
                content2 = requests.get(nameHref,headers).text
                tree2 = etree.HTML(content2)
                year = Data.get_year(tree2)

                path3 = f'//div[@class="title"]/a/@href'
                titleHref = tree1.xpath(path1+path3)[0]
                content3 = requests.get(titleHref,headers).text
                tree3 = etree.HTML(content3)
                location = Data.get_location(tree3)
                room = Data.get_room(tree3)
                area = Data.get_area(tree3)
                avgprice = Data.get_avgPrice(tree3)
                totalprice = Data.get_totalPrice(tree3)


                oldhouseinfo = OldHouseModel(housename=housename,year=year,location=location,room=room,tag=tag,area=area,avgprice=avgprice,totalprice=totalprice)
                oldhouse = {
                    'housename':housename,
                    'year':year,
                    'location':location,
                    'room':room,
                    'tag':tag,
                    'area':area,
                    'avgprice':avgprice,
                    'totalprice':totalprice
                }
                oldhousedata.append(oldhouse)
                try:
                    with app.app_context():
                        db.session.add(oldhouseinfo)
                        db.session.commit()
                        # saveData(oldhousedata)
                        print(f'第{i}条数据插入成功')
                except Exception as e:
                    print(e)
                    print('数据插入失败！')
            else:
                break
    saveData(oldhousedata)

if __name__ == '__main__':
    # get_details_url()
    # print(first_urls)
    crawler()




