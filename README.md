# UiAuto 
***
## 简介：
基于Appium、aircv、tesseract  
实现识别截图上的中文，完成对中文的点击操作；  
实现有目标截图、对比原图的情况下，完成对目标截图的点击操作。
***
## 依赖：
1、[aircv](https://github.com/NetEaseGame/aircv)( *网易开源的项目，基于图像识别，定位到待点击图片位置。*)  
2、[tesseract](https://github.com/tesseract-ocr/tesseract)( *Tesseract Open Source OCR Engine，基于文字识别的引擎。有兴趣的同学可以深入去了解一下。*)  
3、[Appium](http://appium.io)( *Appium的安装我就不再这里赘述了，有问题的小伙伴可以私信我。*)  
***
## 用法：
两个模块：  

1、**click**  
```
def click(self, imgsrc, imgobj):

    imsrc = ac.imread(imgsrc)  # 原始图像
    imsch = ac.imread(imgobj)  # 待查找的部分
    position = ac.find_sift(imsrc, imsch)

    x, y = position['result']

    print("x = ", x)
    print("y = ", y)

    self.driver.swipe(x, y, x, y, 50)  # 点击操作
```

调用例子：  
```    
    imgsrc = 'path to imgsrc.png'
    imgobj = 'path to imgobj.png'
    self.Locate_Image_Click.click(imgsrc, imgobj)
```    
<table><tr><td bgcolor=orange> 背景色是 1 orange</td></tr></table>
2、**click_text**  
```
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
```

调用例子

```

```
