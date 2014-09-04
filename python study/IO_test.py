#-*- coding:utf-8 -*-

'IO study'

#read()会一次性读取文件的全部内容
#read(size)方法，每次最多读取size个字节的内容
#readlines()一次读取所有内容并按行返回list

with open('study01.py', 'rb') as f:
	for line in f.readlines():
		pass
		#print line.strip() 		# 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')

#open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object

#要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码
'''
>>> f = open('/Users/michael/gbk.txt', 'rb')
>>> u = f.read().decode('gbk')
>>> u
u'\u6d4b\u8bd5'
>>> print u
测试
'''

#Python还提供了一个codecs模块帮我们在读文件时自动转换编码
'''
>>> import codecs
>>> with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
>>>    f.read() # u'\u6d4b\u8bd5'
'''

#当我们写文件时，操作系统往往不会立刻把数据写入磁盘，
#而是放到内存缓存起来，空闲的时候再慢慢写入。
#只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘
#with语句会自动调度close方法

#with open('test.txt', 'w') as f:
#	f.write("Hello world")

import os
try:
	print os.uname()
except Exception, e:
	print 'error'

#在操作系统中定义的环境变量，全部保存在os.environ
print os.environ

#要获取某个环境变量的值，可以调用os.getenv()函数
print os.getenv('PATH')

# 查看当前目录的绝对路径:
path = os.path.abspath('.')
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
new_path = os.path.join(path, 'testdir')		#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 然后创建一个目录:
os.mkdir(new_path)
os.rmdir(new_path)

# 对文件重命名:
# 删掉文件:
'''
>>> os.rename('test.txt', 'test.py')
>>> os.remove('test.py')
'''

print os.path.split('/Users/michael/testdir/file.txt')
print os.path.splitext('/path/to/file.txt')

#利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码
print [x for x in os.listdir('.') if os.path.isdir(x)]	
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

print '*********************************'

