# -*- coding: utf-8 -*-

'study07.py including class study'

#类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数和关键字参数

class Student(object):		#()中为该类继承的父类

	def __init__ (self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s: %s' % (self.name, self.score)

std1 = Student('Bob', 90)
std2 = Student('Tom', 95)
std1.print_score()
std2.print_score()

#动态语言的特点就是不需要提前预定义，同一种类型的不同实例，都可能有不同的成员


#****************访问限制********************
#变量名前添加__表示该变量为私有变量
class Person(object):
	def __init__(self, name, sex):
		self.__name = name
		self.__sex = sex

	def printInfo(self):
		print 'name:%s, sex:%s' % (self.__name, self.__sex)

p1 = Person('Jack', 'man')
p1.printInfo()

#_name，这样的实例变量外部是可以访问的，
#但是，按照约定俗成的规定，当你看到这样的变量时
#意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”


#****************继承和多态******************
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
class Animal(object):
	def run(self):
		print "Animal is running!"

class Dog(object):
	def run(self):
		print "Dog is running!"

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())
run_twice(Dog())


#*******************获取对象信息*****************
print type(abs)
#Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入
import types
print type('abc') == types.StringType
print type([]) == types.ListType
#最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType
print type(int) == type(str) == types.TypeType
print type(Dog())


#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print dir('123')
#在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
print len('123')
print '123'.__len__()


#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyObject(object):

	def __init__(self):
		self.x = 9

	def power(self):
		return self.x ** 2

	def __len__(self):
		return 20

obj = MyObject()
print len(obj)

print hasattr(obj, 'x') # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print hasattr(obj, 'y')
print getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
