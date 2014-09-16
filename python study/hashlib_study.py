#-*- coding:utf-8 -*-

#*****************MD5摘要算法****************
import hashlib

#摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
#而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同

#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib')
print md5.hexdigest()


#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
#比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。
sha1 = hashlib.sha1()
sha1.update('how to use md5')
sha1.update(' in python hashlib')
print sha1.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password)
	return md5.hexdigest()

def user_login(name, password):
	for k, v in db.iteritems():
		md5_pwd = calc_md5(password)
		if k == name and v == md5_pwd:
			return True
	return False


if user_login('michael', '123456'):
	print 'OK'
else:
	print 'false'

#由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”
#经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
#如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。	

