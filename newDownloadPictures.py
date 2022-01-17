import requests  # request img from web
import shutil  # save img locally


def download_image(url, file_name):
    # url = "https://p.iimzt.com/2022/01/14k14f.jpg"  # prompt user for img url
    # file_name = '14k14f.jpg'  # prompt user for file_name

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
    else:
        print(res.status_code)
        print(url)
        print('下载失败')


my_list = []
for i in range(0, 10):
    a = str(i)
    for j in range(0, 10):
        b = str(j)
        for h in range(97, 123):
            c = str(chr(h))
            for k in range(0, 10):
                d = str(k)
                for t in range(0, 10):
                    e = str(t)
                    for m in range(97, 123):
                        f = str(chr(m))
                        my_list.append(a + b + c + d + e + f + ".jpg")

for i in my_list:
    download_image("https://p.iimzt.com/2022/01/" + i, i)
