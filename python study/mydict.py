# -*- coding: utf-8 -*-

'python study11.py including unit test'

class Dict(dict):
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("Object Dict doesn't have the attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

#为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py
