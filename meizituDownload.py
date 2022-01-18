# 网站限制1分钟 50 次
import os
import time
import requests
from bs4 import BeautifulSoup


# 妹子图下载

class MeiZiTu:
    def __init__(self):
        self.base_url = "https://www.mmzztt.com/"
        self.headers = {
            "cookie": None,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
            'referer': 'https://mmzztt.com/'
        }
        self.image_url = None
        self.base_path = "~/Downloads/meizitu/"

    # 创建目录
    def create_folder(path):
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

    # 获取图片
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
            for a in a_list:
                image = a.select_one("img")
                print("图片标题: ", image.attrs["alt"])
                print("图片地址: ", image.attrs["data-original"])
                print("详情页链接: ", a.attrs["href"])

                # 创建目录
                path = self.base_path + image.attrs["alt"] + '/'
                self.create_folder(path)

                # 下载图片
                self.download_image(image.attrs["data-original"], path=path, ref=self.base_url)

                # 套图翻页
                next_page = self.get_max_page(url=a.attrs["href"])
                for i in range(1, next_page):
                    url = a.attrs["href"] + "/" + str(i)
                    self.get_images_details(url, path)

            # 翻页
            next_page = soup.select_one(".nav-links > .next")
            if next_page:
                self.get_images(next_page.attrs["href"])
            else:
                pass

    # 获取套图最大地址
    def get_max_page(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            time.sleep(60)
            self.set_cookie()
            self.get_max_page(url)
        else:
            soup = BeautifulSoup(response.text, 'lxml')
            pagenavi = soup.select(".pagenavi > a > span")[-2]
            next_page = pagenavi.string
            return int(next_page)

    # 获取图片详情
    def get_images_details(self, url, path):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code != 200:
            time.sleep(60)
            self.set_cookie()
            self.get_images_details(url, path)
        else:
            soup = BeautifulSoup(response.text, 'lxml')
            image = soup.select_one(".main-image > p > a > img")
            self.download_image(image.attrs["src"], path=path, ref=url)

    # 下载图片
    def download_image(url, path, ref):
        print("正在下载图片:", url)
        headers = {
            "Referer": ref,
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
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
