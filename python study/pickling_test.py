#-*- coding:utf-8 -*-

#我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
#变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

try:
	import cPickle as pickle
except ImportError:
	import pickle

d = dict(name='Bob', age=20, score=88)
print pickle.dumps(d)

with open('dump.txt', 'wb') as f:
	pickle.dump(d, f)

#当我们要把对象从磁盘读到内存时，可以先把内容读到一个str，然后用pickle.loads()方法反序列化出对象，
#也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。

with open('dump.txt', 'rb') as f:
	d = pickle.load(f)

print d
