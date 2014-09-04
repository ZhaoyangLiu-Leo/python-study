#-*- coding:utf-8 -*-

#如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
#因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
#同时参考pickling_test.py

import json

d = {'name': 'Bob', 'age': 20, 'score': 88}
json_str = json.dumps(d)		#转换成json格式的字符串
print json_str

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d = json.loads(json_str)
print d

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

	def __str__(self):
		return self.name + str(self.age) + str(self.score)

def student2json(std):
	return {'name': std.name, 'age': std.age, 'score': std.score}

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Jack', 20, 90)
print json.dumps(s, default=student2json) #如果没有该属性，会抛出异常因为不知道类如何转换成json格式，同理反序列化也需要

#默认将所有类看作dict
print json.dumps(s, default=lambda obj: obj.__dict__)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))