import time
import sys
import requests  # request img from web
import shutil  # save img locally

prefix = sys.argv[1]


# 原来设计第二个参数是张数，到了就停止，现在暂时改成每个参数都是前缀
# numer_image = int(sys.argv[2])
#
# tensDigit = int(int(sys.argv[2]) / 10) + 1


def download_image(url, file_name):
    url = url  # prompt user for img url
    file_name = file_name  # prompt user for file_name
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
        'referer': 'https://mmzztt.com/'
    }

    res = requests.get(url, stream=True, headers=headers)

    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print(url)
        print('下载成功： ', file_name)
        save_result = True
    else:
        print(res.status_code)
        print(url)
        print('下载失败')
        save_result = False
    return save_result


# new_list = []
# for k in range(0, tensDigit):
#     d = str(k)
#     for t in range(0, 10):
#         e = str(t)
#         for m in range(97, 123):
#             f = str(chr(m))
#             new_list.append(d + e + f + ".jpg")
#
# count = 0
#
# for i in new_list:
#     result = download_image("https://p.iimzt.com/2022/01/" + prefix + i, prefix + i)
#     if result:
#         count += 1
#         if count == numer_image:
#             break
#     time.sleep(1.3)  # 增加休眠时间以保证不会同一个ip访问被拒绝

def generate_file_name_list(ten_digit):
    new_list = []
    for k in range(0, ten_digit):
        d = str(k)
        for t in range(0, 10):
            e = str(t)
            for m in range(97, 123):
                f = str(chr(m))
                new_list.append(d + e + f + ".jpg")
    return new_list


count = 0

n = len(sys.argv)

for j in range(1, n):
    if j % 2 != 0:
        prefix = str(sys.argv[j])
        continue
    ten = int(int(sys.argv[j]) / 10) + 1
    my_list = generate_file_name_list(ten)
    for i in my_list:
        result = download_image("https://p.iimzt.com/2022/01/" + prefix + i, prefix + i)
        if result:
            count += 1
        time.sleep(1.4)  # 增加休眠时间以保证不会同一个ip访问被拒绝

sendNotify = "https://sctapi.ftqq.com/SCT108058TYu9gDJyEv4lBTAWwEQGfzAty.send?title=%E4%B8%8B%E8%BD%BD%E7%BB%93%E6%9D%9F&desp=" + str(
    count)

requests.get(sendNotify)
