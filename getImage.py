# coding = utf-8
import re

import requests


def getImage():
    print('正在从网站下载图片')
    # 获取wifi网页内容
    r = requests.get("http://buzzdor.com/identifiants-wifi-gratuit-sfrfreeneuf/")
    # 正则表达式获取所有img标签中的图片地址
    p = re.compile(r'<img[^>]*?src="([^"]*)')
    # 获取第五个图片的地址，第五个图片是正文中的那张图
    image = p.findall(r.text)[4]
    # 获取第五个图片
    ir = requests.get(image)
    # 获取图片名
    imageName = image.split('/')[-1]
    print('下载完成')
    # 保存图片到本地
    sz = open(imageName, 'wb').write(ir.content)
    print('下载的图片名为： ' + str(imageName))
    return imageName
