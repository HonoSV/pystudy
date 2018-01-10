from html.parser import HTMLParser
from urllib import request
import re


class MyHTMLParser(HTMLParser):
    res = []
    flag = 0
    is_get_data = 0

    def handle_starttag(self, tag, attrs):
        # 首先找到包裹事件的元素
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events',attr[1]):
                    self.flag = 1
        # 处理包裹事件名称的a元素
        if tag == 'a' and self.flag == 1:
            self.is_get_data = 'title'
        # 处理时间的time元素
        if tag == 'time' and self.flag == 1:
            self.is_get_data = 'time'
        # 处理包裹地点的span元素
        if tag == 'span' and self.flag == 1:
            self.is_get_data = 'addr'

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'ul':
            self.flag = 0

    def handle_data(self, data):
        if self.is_get_data and self.flag == 1:
            if self.is_get_data == 'title':
                self.res.append({self.is_get_data: data})
            else:
                self.res[len(self.res) - 1][self.is_get_data] = data
            self.is_get_data = 0


with request.urlopen('https://www.python.org/events/python-events/', timeout=4) as f:
    data = f.read()
parser = MyHTMLParser()
result = parser.feed(data.decode('utf-8'))
print('===============================================================================')
for item in MyHTMLParser.res:
    for k,v in item.items():
        print("%s : %s" % (k, v))
