# -*- coding:utf-8 -*-

#Python没有专门处理字节的数据类型。但由于str既是字符串，又可以表示字节

#在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的str



from struct import *

#好在Python提供了一个struct模块来解决str和其他二进制数据类型的转换。
#struct的pack函数把任意数据类型变成字符串：
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
print pack('>I', 10240099)
print unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')

#Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。
s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图； 一个4字节整数：表示位图大小； 
一个4字节整数：保留位，始终为0； 一个4字节整数：实际图像的偏移量； 
一个4字节整数：Header的字节数； 一个4字节整数：图像宽度； 
一个4字节整数：图像高度； 一个2字节整数：始终为1； 一个2字节整数：颜色数。
'''


print unpack('<ccIIIIIIHH', s)