# 导入模块
import Url_Manager
import parser_html
import html_output
import download


class SpiderMain(object):
    def __init__(self):
        # 实例化:url管理器,网页下载器，网页解析器，数据输出
        self.urls = Url_Manager.UrlManager()
        self.parser = parser_html.Htmlparser()
        self.download = download.download()
        self.outputer = html_output.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 向列表里面添加新的单个url
        self.urls.add_new_url(root_url)
        # 判断待爬取的url列表里面有没有新的url
        while self.urls.has_new_url():
            try:
                # 如果待爬取的url列表不为空，则取一个url出来
                new_url = self.urls.get_new_url()
                print('craw %d:%s' % (count, new_url))
                # 下载网页

                html_cont = self.download.download(new_url)
                # 解析网页
                # 解析获得两个数据：新的url，以及我们要获取的数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 获取的url添加到待爬取的url列表

                self.urls.add_new_urls(new_urls)
                # 保存数据
                self.outputer.collect_data(new_data)
                # 如果下载的url页面达到50个，结束当前循环
                if count == 50:
                    break
                count = count + 1
            except:
                print('craw failed')
        # 输出数据
        self.outputer.output_html()


if __name__ == '__main__':
    url = "http://www.dili360.com/gallery/"
    root_url = url
    # 实例化
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)