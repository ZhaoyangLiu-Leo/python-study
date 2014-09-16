# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


class MyHTMLParser(HTMLParser):
	
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
        	if attr[0] == 'class' and attr[1] == 'event-title':
        		print 'meeting title:'
        	elif attr[0] == 'datetime':
        		print 'meeting time: %s' % attr[1]

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('<li><h3 class="event-title"><a href="/events/python-events/162/">Kiwi PyCon 2014</a></h3><p><time datetime="2014-09-12T00:00:00+00:00">12 Sept. &ndash; 15 Sept. <span class="say-no-more"> 2014</span></time><span class="event-location">Wellington, New Zealand</span></p></li>')