# -*- coding: utf-8 -*-

#文档注释

'study05.py module study'
from __future__ import unicode_literals
from __future__ import division

__author__ = 'lzy'

#*****************代码移植过程中__future__模块的使用*********************


print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print 'Hello World!'
	elif len(args) == 2:
		print 'Hello, %s!' % args[1]
	else:
		print 'Too many args!'

if __name__ == '__main__':
	test()

#模块别名的使用
try:
	import cStringIO as StringIO
except ImportError:		#导入失败的话会捕获ImportError
	import StringIO


#******************python作用域****************
#_xxx和__xxx这样的函数或变量就是非公开的（private）
#__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量





