#-*- coding:utf-8 -*-
import os

def search(s, path='.'):
	#print path
	if isinstance(s, str):
		file_dir = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]		#获取当前文件夹下面的所有目录
		file_path = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and (s in x)]		#获取当前文件夹下的包含字符串的文件名
		if file_path:		#list不为空，存在文件，打印文件名
			for p in file_path:
				print os.path.join(path, p)
		if file_dir:		#存在子目录，向下递归
			for d in file_dir:
				#print d
				search(s, os.path.join(path, d))
				#print os.path.join(path, d)

print os.path.abspath('.')
find_str = raw_input('Please input str:')
search(find_str, os.path.abspath('.'))

#实现策略2：利用os.walk函数，实现遍历目录
# os.walk 方便很多了.这个方法返回的是一个三元tupple(dirpath, dirnames, filenames),
#其中第一个为起始路径，
#第二个为起始路径下的文件夹,
#第三个是起始路径下的文件.
#dirpath是一个string，代表目录的路径,
#dirnames是一个list，包含了dirpath下所有子目录的名字,
#filenames是一个list，包含了非目录文件的名字.这些名字不包含路径信息,如果需要得到全路径,需要使用 os.path.join(dirpath, name).