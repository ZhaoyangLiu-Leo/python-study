#coding:utf-8
#python study02 include list, tuple, dic, set

#list study
classmates = ['Mike', 'Jane', 'Joe']
print classmates[-1]

#添加到末尾
classmates.append('Adam')
print classmates

#添加到指定位置
classmates.insert(1, 'Jack')
print classmates

#删除末尾 or 删除某个位置pop(i)
classmates.pop()
print classmates

#更改list，可直接修改
classmates[2] = 'Bob'
print classmates

#list中元素类型可不一致
l = ['A', 2, True, [2, 3]]
print l

#空list判定时，为False
l = []
if l:
    print "not None"
else:
    print "None"



#tuple study
#元素初始化必须指定，指定后不可更改

#只有一个元素时，添加','，消除歧义
t = (1,)
print t

#tuple不变指的是指向不变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 1
print t


#dic study
d = {'Mike': 95, 'Bob': 80, 'Jane': 90}
print d
#key与value一一对应，后续赋值是覆盖原有数值
d['Bob'] = 85
print d

#通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print d.get('Thomas')
print d.get('Thomas', -1)

#dic中的key可以是字符串和整数，不可以是list



#set study
s = set([1, 2, 3])
print s
#set add and remove
s.add(4)
s.add(4)
print s

s.remove(2)
print s

#& and |
s1 = set([1, 2, 4])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2
s1.add((1, 2))
print s1



 
