# coding = utf-8
import os
import time

from PIL import Image


def imageCut(image):
    img = Image.open(image)
    # img.show()
    width = img.size[0]
    height = img.size[1]
    # crop((x,y,x+w,x+y))
    # 距离图片左边界距离x，
    # 距离图片上边界距离y，
    # 距离图片左边界距离+裁剪框宽度x+w，
    # 距离图片上边界距离+裁剪框高度y+h）
    # 切割头部表示区域
    img2 = img.crop((0, 143, width, height))
    # 获得今天的日期
    today = time.strftime("%Y-%m-%d", time.localtime())
    img2FileName = 'wifi_' + str(today + '.jpg')
    # 将文件另存为新文件
    img2.save(img2FileName)
    os.remove(image)
    print('图片' + img.filename + '已删除')
    print('新图片已保存为' + img2FileName)
    return
