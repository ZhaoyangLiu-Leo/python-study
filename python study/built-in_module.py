# -*- coding: utf-8 -*-


#*******************base64******************
#Base64是一种最常见的二进制编码方法。
#Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，
#好处是编码后的文本数据可以在邮件正文、网页等直接显示
#如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，
#再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

import base64

print base64.b64encode('binary\x00string')

print base64.b64decode('YmluYXJ5AHN0cmluZw==')

#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
#所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_

print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')

#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。


def myb64decode(decode_str):
	while len(decode_str) % 4 != 0:
		decode_str = decode_str + "="
	return base64.b64decode(decode_str)

print myb64decode('YWJjZA')