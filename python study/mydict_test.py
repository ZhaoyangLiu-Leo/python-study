# -*- coding: utf-8 -*-

__author__ = 'lzy'

#引入Python自带的unittest模块
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
	#以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEquals(d.a, 1)
		self.assertEquals(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEquals(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	#单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
	def setUp(self):
		print 'setUp...'
	def tearDown(self):
		print 'tearDown...'

#测试方法一，然后再cmd中正常运行即可
#if __name__ == '__main__':
#	unittest.main()

#测试方法二，在cmd中敲入命令：python -m unittest mydict_test


#于此同时，可以通过文档测试来进行测试
#import doctest
#    doctest.testmod()


