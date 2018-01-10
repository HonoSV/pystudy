# -*- coding:utf-8 -*-
from xml.parsers.expat import ParserCreate
from urllib import request
from datetime import datetime


class DefaultSaxHandler(object):
    def __init__(self):
        self.location = {}
        self.args = []

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.location = attrs
        if name == 'yweather:forecast':
            data = {}
            cday = datetime.strftime(datetime.strptime(attrs['date'], '%d %b %Y'), '%Y-%m-%d')
            data['date'] = cday
            data['high'] = attrs['high']
            data['low'] = attrs['low']
            self.args.append(data)

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass


def parseXml(xml_str):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return {
        'city': handler.location['city'],
        'forecast': handler.args
    }


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print(result)