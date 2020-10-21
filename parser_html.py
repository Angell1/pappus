from urllib.parse import urljoin
from bs4 import BeautifulSoup


class Htmlparser(object):

    def _get_new_urls(self, page_url, soup):

        new_urls = set()  # 这里可以加上正则表达式，对url进行过滤
        links = soup.find_all('a')
        for link in links:
            # 补全url,添加到列表里面
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):

        # 解析数据,由用户来编写
        new_datas = set()
        imgs = soup.find_all('img')
        for img in imgs:
            new_data = img['src']
            new_full_data = new_data
            new_datas.add(new_full_data)
        return new_datas

    # 需要解析出新的url和数据
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        # 调用两个本地方法：解析新的url以及解析数据
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

# 报错：
# UserWarning: You provided Unicode markup but also provided a value for from_encoding. Your from_encoding will be ignored.
# 解决方法：
# soup = BeautifulSoup(html_doc,"html.parser")
# 这一句中删除【from_encoding="utf-8"】
# 原因：
# python3 缺省的编码是unicode, 再在from_encoding设置为utf8, 会被忽视掉，去掉【from_encoding="utf-8"】这一个好了