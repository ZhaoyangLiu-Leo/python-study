# -*- coding: utf-8 -*-
#python study04.py,include slice, for, List Comprehensions

#******************切片****************
#tuple、list、字符串都支持切片
L = [0, 1, 2, 3, 4]
print L[0:3] 

#支持倒数切片
name = ['Bob', 'Tom', 'Jack', 'Mike', 'Jane']
print name[-2:]

num = range(100)
print num[:10:2]
print num[::4]
print (1, 2, 3)[0:1]
print 'abcde'[:2]


#******************迭代****************
#只要是可迭代类型即可，不一定是list，如tuple、dic、string
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key

for value in d.itervalues():
	print value

for k, v in d.iteritems():
	print k, v

#用于判定是否是可迭代类型
from collections import Iterable

print 'string:', isinstance('abc', Iterable)
print 'list:', isinstance([1, 2], Iterable)
print 'num:', isinstance(12, Iterable)

#对list实现类似Java那样的下标循环，使用Python内置的enumerate函数
for i, value in enumerate(['a', 'b', 'c']):
	print i, value

#同时使用多个变量
for x, y in ((1, 1), (2, 4), (3, 9)):
    print x, y


#***************列表生成式****************
#生成[1x1, 2x2, 3x3, ..., 10x10]
l1 = [x * x for x in range(1, 11)]
print l1

#添加判断条件
l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print l3

#打印效果为双重循环
l2 = [x * y for x in range(1, 11) for y in range(2, 12)]
print l2	

#列出当前目录下的所有文件和目录名
import os
print [d for d in os.listdir('g:/Python/')]

#列表生成式同时生成两个数据
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]

print 'ABC'.lower()

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]



#**************生成器**********************
#Python中，这种一边循环一边计算的机制，称为生成器（Generator）
#生成器实现方式1
g = (x * x for x in range(10))
print g.next()
for n in g:
	print n

#生成器实现方式2，执行到yield语句返回，当调用next时候再度进入函数
def fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

for n in fab(6):
	print n

a, b = 3, 5
a, b = b, a
print a, b