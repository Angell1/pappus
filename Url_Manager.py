
# url管理器需要四个方法：
# add_new_url:向管理器添加单个url
# add_new_url:向管理器添加批量的url
# has_new_url:判断管理器里面是否有新的在爬取的url
# get_new_url:在管理器中获取一个正在爬取的url
# url管理器需要维护两个列表：待爬取的url，已经爬取的url


class UrlManager(object):
    def __init__(self):
        # 待爬取的url列表
        self.new_urls = set()
        # 已经爬取的url列表
        self.old_urls = set()

    # 向管理器添加单个url
    def add_new_url(self, url):
        # 首先判断url是否为空
        if url is None:
            return
        # 如果这个url既不在待爬取的url里面也没有在已经爬取的url里面，则说明这是一个新url
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器添加批量的url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断管理器里面是否有新的在爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一个正在爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url