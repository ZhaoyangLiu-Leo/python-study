#-*- coding:utf-8 -*-

'study08.py 包含面向对象高级编程'

#通常情况下，下面的set_score方法可以直接定义在class中，
#但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
from types import MethodType

class Student(object):
	def __init__(self, name):
		self.name = name
		self.score = 40

def set_score(self, score):
	self.score = score

#给student类添加方法，因此第二个参数为None
Student.set_score = MethodType(set_score, None, Student)
s = Student('Mike')
s.set_score(20)
print s.score

#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
#__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
class Person(object):
	__slots__ = ('name', 'age')
	pass
#子类如果不定义__slots__的话，则添加属性不受限，如果添加后，则受父类和子类共同的限制
#总之，为父类和子类的并集
class Worker(Person):
	__slots__ = ('age')
	pass

p = Person()
p.name = 'Mike'
p.age = 18
#p.sex = 'man'
print p.name, p.age

w = Worker()
w.name = 'John'
print w.name

#****************@property****************
#Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Student2(object):

	def name():
	    doc = "The name property."
	    def fget(self):
	        return self._name
	    def fset(self, value):
	        self._name = value
	    def fdel(self):
	        del self._name
	    return locals()
	#name = property(**name())


s = Student2()
s.name = 'Mike'
print s.name
#s.name = 123
#print s.name

class Person2(object):
    def __init__(self, age):
    	self._age = age
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be string')
        else:
            self._name = value
    #如果没有setter方法的话，属性仅为可读属性       
    @property
    def age(self):
    	return self._age


p = Person2(15)
p.name = '123'
print p.name
#p.age = 15
print p.age


#python支持多继承

#*******************定制类**********************
class Student3(object):
	def __init__(self, name):
		self.__name = name
	def __str__(self):
		return "student: %s" % self.__name

	__repr__ = __str__

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 25
	#定义一个__call__()方法，就可以直接对实例进行调用
	def __call__(self):
		return 'My name is %s' % self.__name

s = Student3('Mike')
print s
print dir(s)

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己

	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100:
			raise StopIteration()
		return self.a

	#实现如list那样获取某个元素或者子list
	def __getitem__(self, n):	#__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
		a, b = 1, 1
		if isinstance(n, int):			
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L



	#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，好需要实现__getitem__

for n in Fib():
	print n

f = Fib()
print f[2]
print f[2:5]

s = Student3('Joe')
print 'score:', s.score
print 'age:', s.age()
print 'student3 is called directly', s()
#判断对象是否是可调用类型Callable
print callable(s)
print callable([1, 2, 3])

#通过__getattr__实现动态链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print Chain().status.user.timeline.list

#我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类
def fn(self, name='world'):
	print 'Hello, %s' % name

Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()

class Temp(object):
	name = 'Temp'		#类属性
	def __init__(self, name):
		self._name = name 	#实例属性，实例属性优先级高于类属性



