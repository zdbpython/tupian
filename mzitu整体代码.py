# -*- coding:UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import os
from urllib import request
import os.path
import time



def down_pic(url, path):  # 下载图片函数
    headers = {'Referer': url,
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
               }
    try:
        req = request.Request(url, headers=headers)# 对图片地址加请求头
        data = request.urlopen(req).read()
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(str(e))

def down_img(target_url1) :   #套图下载
    target_url = target_url1+"/"
    target_url = target_url.strip(" ")
    headers = {'Referer': 'https://www.mzitu.com/',
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
               }
    # print(target_url)
    img_req = requests.get(url=target_url, headers=headers)
    img_req.encoding = 'utf-8'
    img_html = img_req.text
    img_bf_2 = BeautifulSoup(img_html, 'lxml')  # 打开图片页面
    # print(img_bf_2)
    # print(img_bf_2)
    # img_num1 = img_bf_2.find(class_="pagenavi")
    # print(img_num1)

    # img_num = img_num1[1].find('a')  # 反复使用find_all
    # img_num  = img_num1.strip("href=")

    # print(img_num)
    # print(img_num[5])
    img_name = img_bf_2.find("title")  # 图片名字
    img_name = str(img_name)
    # print(str(img_name))
    img_name = img_name.strip("</<title>")  # 替换<title>
    # print(img_name)
    img_name = img_name.split("-")  # 分割字符串
    # print(img_name)
    name标题 = img_name[0]  # 取第一个元素
    name标题 = name标题.replace(" ", "")
    print("开始下载套图：{}".format(name标题))
    try:
        os.makedirs(name标题)
        print("已创建{}文件夹".format(name标题))
        aaa=1
    except:
        print("已存在{}文件夹".format(name标题))
        aaa=3
    while aaa > 2 :
        break
    else :
        for num in range(1, 300):  # 循环结构
            if num == 1:
                url1 = target_url
            else:
                num = str(num)
                url1 = target_url + num
                # print(url1 )
            headers = {'Referer': 'https://www.mzitu.com/',
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
                       }
            # print(url1)
            # response = requests.get(url1)

            img_req = requests.get(url=url1, headers=headers)
            img_req.encoding = 'utf-8'
            img_html = img_req.text
            img_bf_1 = BeautifulSoup(img_html, 'lxml')  # 打开图片页面
            # print(img_bf_1)
            try:
                img_url = img_bf_1.find('div', 'main-image').img.get('src')  # 图片下载链接
            except:
                break
            # print(img_url)
            # print("当前图片链接：{}".format(img_url))
            img_bf_2 = BeautifulSoup(img_html, 'lxml')  # 打开图片页面
            # print(img_bf_2)
            img_name = img_bf_2.find("title")  # 图片名字
            img_name = str(img_name)
            # print(str(img_name))
            img_name = img_name.strip("</<title>")  # 替换<title>
            # print(img_name)
            img_name = img_name.split("-")  # 分割字符串
            # print(img_name)
            img_name = img_name[0]  # 取第一个元素
            # print(img_name)

            img_name = img_name.strip()
            # print("当前图片名字：{}".format(img_name))

            filename = img_name + '.jpg'
            # print(filename)

            time.sleep(1)

            path = os.path.join(name标题, filename)
            path = path.replace(" ", "")
            # print(path)

            down_pic(img_url, path)

            print('下载完成图片:{}'.format(img_name))
        print('下载完成套图:{}'.format(name标题))





if __name__ == '__main__':      #主程序，爬取链接
    list_url = []
    str开始 = input("输入起始页码：");
    str结束 = input("输入结束页码：");
    print("输入的起始页码为{},结束页码为{} ".format(str开始,str结束))
    str开始 = int(str开始)
    str结束 = int(str结束)
    str结束 = str结束 + 1
    for num in range(str开始,str结束):#循环结构
        if num == 1:
            url = 'https://www.mzitu.com/'
        else:
            url = 'https://www.mzitu.com/page/%d' % num
        headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
        }
        req = requests.get(url=url, headers=headers)
        req.encoding = 'utf-8'
        html = req.text
        print(url)
        # print(html)
        bf = BeautifulSoup(html, 'lxml')
        # print(bf)
        targets_url = bf.find_all(id="pins")
        # targets_url = bf.find_all("span")
        #print(type(targets_url))
        name1 = targets_url[0].find_all('a')  # 反复使用find_all
        #print(name1)
        # print(targets_url)

        for each in name1:
            list_url.append(each.get('href'))  # 获取当前页面链接
        list_url = list(set(list_url))
    #print(list_url)
    print("已获取套图链接")
    for xurl in list_url:
        down_img(xurl)
