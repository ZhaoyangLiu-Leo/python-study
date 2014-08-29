# -*- coding:utf-8 -*-

'study09.py including exception'

#我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
#错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理
#Python所有的错误都是从BaseException类，如果能先捕捉到其父类的exception，子类无法捕捉
try:
	print 'try'
	r = 10 / int('a')
	print 'result:', r
except Exception, e:
	print 'error:', e
else:
	print 'no error'
finally:
	print 'finally'

print 'end'

#Python内置的logging模块可以非常容易地记录错误信息，如果不记录的话，程序会因为异常而终止	
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'

#可以自定义异常类，但是尽量使用内置的异常类
#class FooError(StandardError):
#    pass

#def foo(s):
#    n = int(s)
#    if n==0:
#        raise FooError('invalid value: %s' % s)
#    return 10 / n

#foo('0')

#except后继续raise，是因为捕获错误目的只是记录一下，便于后续追踪。
#但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理
#raise可以抛出不同类型的异常
def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise ValueError('input error!')


#凡是用print来辅助查看的地方，都可以用断言（assert）来替代
#不过，启动Python解释器时可以用-O参数来关闭assert
#def temp(s):
#	n = int(s)
#	assert n != 0, 'n is zero'
#	return 10 / n

#temp('0')
#logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n


