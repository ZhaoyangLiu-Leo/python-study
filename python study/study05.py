#coding:utf-8

#**************高阶函数*****************
#************传入函数，函数作为参数*********

def f(x):
	return x * x

a = [1, 2, 3, 4]
b = map(f, a)
print b

#像map()函数这种能够接收函数作为参数的函数，称之为高阶函数（Higher-order function）


#把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
	return x * 10 + y

a = reduce(fn, [1, 3, 5, 7, 9])
print a

#str转换成int
def str2int(s):
	return reduce(fn, map(int, s))

print str2int('13579')

#用lambda函数进一步简化
def strToint(s):
	return reduce(lambda x, y: x*10+y, map(int, s))

print strToint('1344')

#python 内置排序sorted()，其本身是高阶函数，参数可传入函数
l = [36, 5, 2, 3, 5]
print sorted(l)

#自定义排序规则
def reversed_cmp(x, y):
	if x > y:
		return -1
	elif x < y:
		return 1
	else:
		return 0

print sorted(l, reversed_cmp)

#自定义忽略大小写大字符串排序
def cmp_ignore_case(s1, s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	elif u1 > u2:
		return 1
	else:
		return 0

print sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)


#************函数作为返回值，函数作为参数*********
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
#每次调用都返回不同的函数，并且使用互不影响
f1 = lazy_sum(*(1, 3, 4, 5))
print f1
print f1()


#******************my_map******************
from collections import Iterable
def my_map(fun, l):
	if not isinstance(l, Iterable):
		 raise TypeError("argument 2 must be a iterable")
	#res = []
	#for n in l:
	#	res.append(fun(n))
	#return res
	return [fun(x) for x in l]

#my_map(f, [1, 2, 3, 4])
res = my_map(f, [1, 2, 3, 4])
print res

#*****************匿名函数******************
#lambda实现匿名函数，":"前的表示参数
func = lambda x: x * x
print f(5)

func = lambda x, y: x + y
print func(3, 5)


#****************装饰器*******************
#代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#两层嵌套实现的装饰器
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

@log
def now():
	print '2014-8-8'

now()
print now.__name__

#三层嵌套实现的装饰器
def log2(text=''):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s call %s():' % (text, func.__name__)
			func(*args, **kw)
			print 'end call %s():' % func.__name__
			return
		return wrapper
	return decorator

@log2('begin')
def time():
	print '2014-8-8'

time()
print time.__name__

#**************************偏函数(Partial function)********************
#简单总结functools.partial的作用就是，把一个函数的某些参数（不管有没有默认值）给固定住（也就是设置默认值），
#返回一个新的函数，调用这个新函数会更简单。
print int('12345', base=8)
import functools
int2 = functools.partial(int, base=2)
print int2('1010101')