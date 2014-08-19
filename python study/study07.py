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