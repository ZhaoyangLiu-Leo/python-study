#coding:utf-8
#python study03，主要包含函数的使用
import math

#for 循环
for x in range(5):
    print x

#函数
print abs(-5)

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print a(-5)

#****************函数定义******************
def my_abs(num):
	#pass 表示什么也不做，用以占位
	#pass
	#添加类型检验
	if not isinstance(num, (int, float)):
		raise TypeError('bad operand type')
	if (num >= 0):
		return num
	else:
		return -num

print my_abs(-6)
#print my_abs('A')

#函数返回多个返回值，其实是返回一个元组
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi/4)
t = move(100, 100, 60, math.pi/4)
print int(x), int(y)
print t

#*****************函数参数*****************
#默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print power(5)
print power(5, 3)

#函数默认参数一定要是不可变对象

#可变参数函数，默认以元组形式传入
def calc(*numbers):
	s = 0
	for n in numbers:
		s = s + n * n
	return s

print calc(1, 2, 3)
l = [1, 2, 3]
print calc(*l)


#*******************关键字参数********************
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw

person('Mike', 18)
person('Bob', 20, city='Beijing')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

#在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。


#****************参数的组合使用******************
def func(a, b, c=0, *args, **kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2)
func(1, 2, 3)  
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)



#****************递归函数*********************
def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)

print '5! =', fact(5)

#递归时调用函数栈，由于受栈的限制，递归次数有限，但是可以通过尾递归进行优化





