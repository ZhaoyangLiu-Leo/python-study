# -*- coding: utf-8 -*-
  

#输入命令l来查看代码
#输入命令n可以单步执行代码输入命令n可以单步执行代码
#任何时候都可以输入命令p 变量名来查看变量

import pdb
'pdb find error code'
s = '0'
n = int(s)
pdb.set_trace()
print 10 / n

#还有一种策略也是用pdb，但是不需要单步执行，我们只需要import pdb，
#然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
#用命令c继续运行