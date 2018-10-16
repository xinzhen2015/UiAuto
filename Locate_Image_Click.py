# -*- coding: UTF-8 -*-

import os
import aircv as ac
from time import sleep
from appium import webdriver


def click(self, imgsrc, imgobj):

    '''
    @Time    : 2018/9/17
    @Author  : 诸葛小心
    @File    : Locate_Image_Click.py

    instruction:
    基于aircv图像识别，传入待查找的图片、原图，则定位到带查找图片在原图上的坐标点

    usage:
    imgsr = 'imgsr.png'
    imgobj = 'imgobj.png'
    self.Locate_Image_Click.click(imgsrc, imgobj)
    '''

    imsrc = ac.imread(imgsrc)  # 原始图像
    imsch = ac.imread(imgobj)  # 待查找的部分
    position = ac.find_sift(imsrc, imsch)

    # print(position)

    x, y = position['result']

    print("x = ", x)
    print("y = ", y)

    self.driver.swipe(x, y, x, y, 50)


def click_text(self, text, imagename):

    '''
    @Time    : 2018/10/16
    @Author  : 诸葛小心
    @File    : Locate_Image_Click.py

    instruction:
    基于tesseract识别出文字(不同语言有不同的文字识别库，此处用的是中文库 chi_sim，主要用于识别中文 )，
    返回文字在屏幕上的坐标点，点击坐标点。

    usage:
    imgsr = 'imgsr.png'
    imgobj = 'imgobj.png'
    self.Locate_Image_Click.click_text(self, '待查找文字'， '屏幕截图的名字')
    '''

    sleep(1)
    h = self.driver.get_window_size()['height']    # 获取屏幕高度
    self.driver.get_screenshot_as_file(imagename)  # 截屏保存在执行脚本文件夹

    if len(text) is None:
        print('请输入需要点击的文字，目前最多支持2个字！')

    elif len(text) == 1:

        if os.path.isfile(imagename):
            os.system('tesseract {} out -l chi_sim makebox'.format(imagename))
            print("输出坐标文件 : out.box")
        else:
            print("{} not found.format(" + imagename + ")")

        list1 = []  # 创建列表，用于存储要点击的文字的位置信息

        if os.path.isfile('out.box'):
            with open('out.box') as f:
                for line in f:
                    if line.split()[0] in text:
                        list1.append(line.split())

        x = (int(list1[0][1]) + int(list1[0][3]))/2
        print(text + ' X坐标为：', x)

        y = int((h - int(list1[0][2])) + (h - int(list1[0][4])))/2
        print(text + ' Y坐标为：', y)

        self.driver.swipe(x, y, x, y, 50)

    elif len(text) == 2:
        if os.path.isfile(imagename):
            os.system('tesseract {} out -l chi_sim makebox'.format(imagename))
            print("输出坐标文件 : out.box")
        else:
            print("{} not found.format(" + imagename + ")")

        list2 = []

        if os.path.isfile('out.box'):
            with open('out.box') as f:
                for line in f:
                    if line.split()[0] in text:
                        list2.append(line.split())

        point_mid_x1 = (int(list2[0][1]) + int(list2[0][3]))/2  # 第一个字的X轴中间点
        point_mid_x2 = (int(list2[1][1]) + int(list2[1][3]))/2  # 第二个字的X轴中间点

        x = (point_mid_x1 + point_mid_x2)/2
        print(text + ' X坐标为：', x)

        # 一般认为第一个字和第二个字的中间点Y轴是一样的，所以取一个字的Y轴就可以了
        y = int((h - int(list2[0][2])) + (h - int(list2[0][4])))/2
        print(text + ' Y坐标为：', y)

        self.driver.swipe(x, y, x, y, 50)

    elif len(text) == 3:
        if os.path.isfile(imagename):
            os.system('tesseract {} out -l chi_sim makebox'.format(imagename))
            print("输出坐标文件 : out.box")
        else:
            print("{} not found.format(" + imagename + ")")

        list3 = []

        if os.path.isfile('out.box'):
            with open('out.box') as f:
                for line in f:
                    if line.split()[0] in text:
                        list3.append(line.split())

        point_mid_x1 = (int(list3[0][1]) + int(list3[0][3]))/2  # 第1个字的X轴中间点
        point_mid_x2 = (int(list3[1][1]) + int(list3[1][3]))/2  # 第2个字的X轴中间点
        point_mid_x3 = (int(list3[2][1]) + int(list3[2][3]))/2  # 第3个字的X轴中间点

        x = (point_mid_x1 + point_mid_x2 + point_mid_x3)/2
        print(text + ' X坐标为：', x)

        # 一般认为三个字的中间点Y轴是一样的，所以取一个字的Y轴就可以了
        y = int((h - int(list3[0][2])) + (h - int(list3[0][4])))/2
        print(text + ' Y坐标为：', y)

        self.driver.swipe(x, y, x, y, 50)

    else:
        print('目前最多支持3个字！')
