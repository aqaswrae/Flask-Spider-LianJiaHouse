#用来写爬虫文件
# 每个都封装成一个函数，保存到数据库的同时，也生成json文件，用来做pyecharts的数据可视化
import time,datetime
import requests,json
# from app import app
from lxml import etree
from models import NewHouseModel
from exts import db
from werkzeug.utils import import_string



app = import_string('app.app')


def a():
    print(time.strftime('%Y-%m-%d %X'))
    # return time.strftime('%Y-%m-%d %X')
# 如何周期性的自动启动运行？？？
def func1():
    print(time.strftime('%Y-%m-%d %X'))
    print('爬虫程序要疯狂的运转了！！！')

def new_timer(h,m):
    while True:
        now = datetime.datetime.now()
        # print(now.hour,now.minute)
        if now.hour == h and now.minute == m:
            func1()
            crawler()
            time.sleep(60)

#在爬虫程序的函数中分别获取到表中的各字段的值， 然后用newhouseinfo=NewHouseMoudel(...)->db.session.add(newhouseinfo)->db.session.commit()保存到数据库
# 同时也要生成json文件供pyecharts来进行数据可视化
# housename = '//div[@class="resblock-name"]/a/text()'  # 第一层网址
# developer = '//ul[@class="x-box"][1]/li[7]/span[2]/text()'  # 第三层网址
# location = '//div[@class="resblock-location"]/span[1]/text()'  # 第一层网址
# room = '//a[@class="resblock-room"]/span/text()'  # 第一层网址
# ty = '//div[@class="resblock-name"]/span[@class="resblock-type"]/text()'  # 第一层网址
# tag = '//ul[@class="x-box"][1]/li[3]/span[2]/text()'  # 第三层网址
# area = '//div[@class="resblock-area"]/span/text()'  # 第一层网址
# avgprice = '// div[ @class ="main-price"]/span[1]/text()'  # 第一层网址
# totalprice = '//div[@class="second"]/text()'  # 第一层网址

#定义一个放静态函数的类
class Data:
    @staticmethod
    def get_Name(path,tree):
        p = '//div[@class="resblock-name"]/a/text()'
        substances = tree.xpath(path + p)
        print(substances[0])
        return substances[0]
    @staticmethod
    def get_Developer(tree):
        developer = '//ul[@class="x-box"][1]/li[7]/span[2]/text()'  # 第三层网址
        substances = tree.xpath(developer)
        strr = ''
        if substances:
            print(substances[0])
            return substances[0]
        else:return strr
    @staticmethod
    def get_Location(path,tree):
        p = '//div[@class="resblock-location"]/span[1]/text()'
        substance = tree.xpath(path + p)
        if substance:
            a = substance[0]
            print(a)
            return a
    @staticmethod
    def get_Room(path,tree):
        p = '//a[@class="resblock-room"]/span/text()'
        substances = tree.xpath(path + p)
        strr = ''
        for i in substances:
            strr += i + '/'
        print(strr)
        return strr
    @staticmethod
    def get_Ty(path,tree):
        p = '//div[@class="resblock-name"]/span[@class="resblock-type"]/text()'
        substances = tree.xpath(path + p)
        strr = ''
        if substances:
            print(substances[0])
            return substances[0]
        else:return strr
    @staticmethod
    def get_Tag(tree):
        tag = '//ul[@class="x-box"][1]/li[3]/span[2]/text()'  # 第三层网址
        substances = tree.xpath(tag)
        strr = ''
        if substances:
            print(substances[0])
            return substances[0]
        else:return strr

    @staticmethod
    def get_Area(path,tree):
        p = '//div[@class="resblock-area"]/span/text()'
        substances = tree.xpath(path + p)
        strr = ''
        if substances:
            print(substances[0][2:].replace('㎡',''))
            return substances[0][2:].replace('㎡','')
        else:return strr
    @staticmethod
    def get_Avgprice(path,tree):
        p_Avgprice1 = '// div[ @class ="main-price"] / span[1]/text()'
        strr = tree.xpath(path + p_Avgprice1)
        if strr:
            print(strr[0])
            return strr[0]
    @staticmethod
    def get_Totalprice(path,tree):
        p = '//div[@class="second"]/text()'
        substances = tree.xpath(path + p)
        strr = ''
        if substances:
            print(substances[0][2:].replace('(万/套)',''))
            return substances[0][2:].replace('(万/套)','')
        else:return strr

homeUrl = 'https://qd.fang.lianjia.com'
baseUrl = 'https://qd.fang.lianjia.com/loupan/pg'
xiangqing = 'xiangqing/'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
filepath = 'D:/Pycharm--professional/code/Flask学习/dataspider'
#第一层网页的网址
first_urls = []
for num in range(1,31):
    u = baseUrl+str(num)
    first_urls.append(u)


def get_details_url():
    url = 'https://qd.fang.lianjia.com/loupan/pg1'
    # 第二层网页的网址
    second_urls = []
    # 第三层网页的网址
    third_urls = []
    a = ['https://qd.fang.lianjia.com/loupan/pg1']
    for i in a:#first_urls:
        content = requests.get(i,headers).text
        # print(content)
        tree = etree.HTML(content)
        for j in range(1,31):
            p = f'//ul[@class="resblock-list-wrapper"]/li[{j}]/a/@href'
            imgahref = tree.xpath(p)
            # print(imgahref)
            if imgahref:
                second_url = homeUrl + imgahref[0]
                third_url = second_url + xiangqing
                second_urls.append(second_url)
                third_urls.append(third_url)
            else:
                break
    #返回两个列表，存储着相应的网址
    return second_urls,third_urls

#保存数据为json文件
def saveData(newhousedata):
    with open(f'{filepath}/newhousedata.json','w',encoding='utf-8') as f:
        json.dump(newhousedata,f,ensure_ascii=False)
newhousedata = []
def crawler():
    for page in range(39,40):
        print(f'============第{page}页============')
        url = baseUrl + str(page)
        content1 = requests.get(url,headers).text
        tree1 = etree.HTML(content1)
        for i in range(1,31):
            path1 = f'//ul[@class="resblock-list-wrapper"]/li[{i}]'
            judge = tree1.xpath(path1)
            if judge:
                housename = Data.get_Name(path1,tree1)
                location = Data.get_Location(path1,tree1)
                room = Data.get_Room(path1,tree1)
                ty = Data.get_Ty(path1,tree1)
                area = Data.get_Area(path1,tree1)
                avgprice = Data.get_Avgprice(path1,tree1)
                totalprice = Data.get_Totalprice(path1,tree1)

                path2 = f'//ul[@class="resblock-list-wrapper"]/li[{i}]/a/@href'
                imgahref = tree1.xpath(path2)
                two_url = homeUrl + imgahref[0]
                three_url = two_url + xiangqing
                content2 = requests.get(three_url,headers).text
                tree2 = etree.HTML(content2)
                developer = Data.get_Developer(tree2)
                tag = Data.get_Tag(tree2)
                newhouseinfo = NewHouseModel(housename=housename,developer=developer,location=location,room=room,ty=ty,tag=tag,area=area,avgprice=avgprice,totalprice=totalprice)
                newhouse = {
                    'housename':housename,
                    'developer':developer,
                    'location':location,
                    'room':room,
                    'ty':ty,
                    'tag':tag,
                    'area':area,
                    'avgprice':avgprice,
                    'totalprice':totalprice
                }
                newhousedata.append(newhouse)
                try:
                    with app.app_context():
                        db.session.add(newhouseinfo)
                        db.session.commit()
                        print(f'第{i}条数据插入成功')
                except Exception as e:
                    print(e)
                    print('数据插入失败！')
            else:
                break
    saveData(newhousedata)

# crawler()


if __name__ == '__main__':
    # get_details_url()
    # print(first_urls)
    crawler()