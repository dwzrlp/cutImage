from PIL import Image

img = Image.open('freesxstylers-31.jpg')

width = img.size[0]
height = img.size[1]
# crop((x,y,x+w,x+y))
# 距离图片左边界距离x，
# 距离图片上边界距离y，
# 距离图片左边界距离+裁剪框宽度x+w，
# 距离图片上边界距离+裁剪框高度y+h）
img2 = img.crop((0, 143, width, height))
