'''
https://book.douban.com/subject_search?search_text=python&cat=1001&start=%s0
使用selenium爬取页面
保存内容
'''

from selenium import webdriver
import time
from lxml import etree

def get_web(url):
    driver = webdriver.Chrome()
    driver.get(url)

    print('waiting for ......')
    time.sleep(40)
    print('waiting for ......')

    driver.save_screenshot('douban_reader.png')

    fn = 'douban-reader.html'
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    content_parse(fn)
    driver.quit()

def content_parse(fn):
    html = ''

    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    tree = etree.HTML(html)

    books = tree.xpath('//div[@class="item-root"]')

    for book in books:
        book_name = book.xpath(".//div[@class='title']/a")
        print(book_name[0].text)

if __name__ == '__main__':
    url = "https://book.douban.com/subject_search?search_text=python&cat=1001&start=%s0"
    get_web(url)