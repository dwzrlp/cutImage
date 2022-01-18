# 网站限制1分钟 50 次
import re
import os
import time
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, wait

# 创建了一个线程池（最多5个线程）
pool = ThreadPoolExecutor(5)


# 妹子图下载
class MeiZiTu():
    def __init__(self):
        self.base_url = "https://www.mmzztt.com/"
        self.image_url = None
        self.base_path = "~/Downloads/meizitu/"

        self.headers = {
            "cookie": None,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
            'referer': 'https://mmzztt.com/'

        }

    # 创建目录
    def create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass

    # 设置cookies
    def set_cookie(self):
        response = requests.get(url=self.base_url, headers=self.headers)
        cookie_list = []
        for key, value in response.cookies.items():
            cookie_list.append(key + "=" + value)
        self.headers["cookie"] = '; '.join(cookie_list)

    # 获取图片列表
    def get_images(self, url=None):
        url = url if url else self.base_url
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            time.sleep(60)
            self.set_cookie()
            self.get_images(url)
        else:
            soup = BeautifulSoup(response.text, 'lxml')
            a_list = soup.select(".postlist > ul > li > a")
            for a in a_list[1:4]:
                image = a.select_one("img")
                print("图片标题: ", image.attrs["alt"])

                # 创建目录
                path = self.base_path + image.attrs["alt"] + '/'
                self.create_folder(path)

                # 下载小图图片
                self.download_image(image.attrs["data-original"], path=path, ref=self.base_url)

                # 获取套图列表
                image_url_list = []
                max_page, image_url = self.get_max_page(url=a.attrs["href"])
                print(image_url)
                file_name = str(image_url).split('/')[-1]
                prefix = str(image_url).replace(file_name, '')
                name = re.findall("\D+", file_name)
                res = re.findall("\d+", file_name)[0]
                for i in range(1, max_page + 1):
                    if i < 10:
                        i = "0" + str(i)
                    else:
                        i = str(i)
                    ref = a.attrs["href"] if i == 1 else a.attrs["href"] + "/" + str(i)
                    data = {
                        "image_url": prefix + res + name[0] + i + name[1],
                        "ref": ref
                    }
                    image_url_list.append(data)

                # 多线程调用下载函数
                tasks = [pool.submit(self.download_image, data["image_url"], path, data["ref"]) for data in
                         image_url_list]
                wait(tasks)

            # 翻页
            # next_page = soup.select_one(".nav-links > .next")
            # if next_page:
            #     self.get_images(next_page.attrs["href"])
            # else:
            #     pass

    # 获取套图最大地址&第一张图片的地址
    def get_max_page(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            time.sleep(60)
            self.set_cookie()
            self.get_max_page(url)
        else:
            soup = BeautifulSoup(response.text, 'lxml')
            pagenavi = soup.select(".pagenavi > a > span")[-2]
            image = soup.select_one(".main-image > p > a > img")
            max_page = int(pagenavi.string)
            return max_page, image.attrs["src"]

    # 下载图片
    def download_image(self, url, path, ref):
        print("正在下载图片:", url)
        headers = {
            "Referer": ref,
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        print(headers)
        video_name = str(url).split('/')[-1]
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            pass
        else:
            file_path = path + str(video_name)
            with open(file_path, mode='wb') as f:
                f.write(response.content)


if __name__ == '__main__':
    meizitu = MeiZiTu()
    meizitu.get_images()

"""
https://imgpc.iimzt.com/2020/05/28b06.jpg
"""
