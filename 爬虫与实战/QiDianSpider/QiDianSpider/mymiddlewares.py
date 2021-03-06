from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse

class QDReaderMiddleware(object):
    def __init__(self):

        self.driver = webdriver.PhantomJS()

    def process_request(self, request, spider):
        '''

        :param request:
        :param spider:
        :return:
        '''
        # 只处理情况页面
        if request.meta.get('phantomjs', True):
            print('正在执行中间件')
            self.driver.get(request.url)
            time.sleep(1)
            html = self.driver.page_source
            # print(html)

            return HtmlResponse(url=request.url, body=html, encoding='utf-8',request=request)