#coding:utf-8
#python study01, including string, input, hex data, r, ''', ...

#字符串打印，","相当于" "
print "hello", "world,", 'I', "like", "python"

#数据输入
#name = raw_input('Please enter your name:')
#print name

#hex data
a = 0x00ff
print a

#r instead of many '\'
print r'\\\t\\'

#''' instead of \n
print '''line1
line2
line3'''

#python 字符串机制
a = 'ABC'
b = a
a = 'XYZ'
print b

#pythoy 字符和对应数字的转换
a = ord('A')
b = chr(65)
print a, b

#字符串编码

#change Unicode to utf-8
print u'ABC'.encode('utf-8')

#change utf-8 to Unicode
print 'abc'.decode('utf-8')

#格式化，当不明确用什么的时候，%s通用
a = 'world'
print 'Hello, %s' % a
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print 'PI is %.2f' % 3.1415