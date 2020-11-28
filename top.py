# coding=utf-8
import sys
import re                                           # 正则表达式，进行文字匹配
import urllib.response, urllib.request, urllib.error   # 指定url，获取网络数据
import bs4                       # 网页解析，获取数据
import xlwt                                          # 进行excel操作
import sqlite3    # 进行sqlite数据库操作
 


def main():
    baseurl = "https://live.kuaishou.com/profile/xiehaichao5201315"
    # 2.爬取网页
    datalist = getData(baseurl)

    # 4、保存数据
    savepath = ".\\top.xls"


# 2.爬取网页

def getData(baseurl):
    datalist = []
    # 3、逐一解析数据
    return datalist

 # 4、保存数据
def saveData(savepath):





if __name__ == "__main__":   #当程序执行时
    #调用函数
    main()


response = urllib.request.urlopen("https://live.kuaishou.com/u/xiehaichao5201314")
print(response.read().decode('utf-8'))
