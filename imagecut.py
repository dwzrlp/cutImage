from PIL import Image

img = Image.open('freesxstylers-31.jpg')

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

# 保存图片


# 截取图片文件名的序号
imgNumber = img.filename.split('-')[1]
# 重新命名文件名 wifi-加序号
img2FileName = 'wifi-' + imgNumber
# 将文件另存为新文件
img2.save(img2FileName)
