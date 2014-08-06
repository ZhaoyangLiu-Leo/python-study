#list test

#create list
mt_list = []
print mt_list

l1 = [[1, 2, 3]]
l2 = ['John', 'Mike', 'Tom']
l3 = [[1, 2, 3], ['Hello', 'World!']]
l4 = [1, 2, 3]
l5 = l1


print l1
print l2
print l3
l1 = l1 + [5, 6]
print 'l1 + [5, 6]:', l1
print 'the first element of l1:', l1[0]
print 'the last element of l2:', l1[-1]

print 'Compare l1 and l4:', l1 is l4
print 'Compare l1 and l5:', l1 is l5

#string is wrong, it doesn't support to alter
#str = 'hello'
#str[0] = 'p'
#print str

print len(['a', 'b', 'c'])
print 'the index of element "2"', l1.index(2)

if 3 in l1:
    print 'Correct!'

print range(14, 1, -3)
print range(2 , 16, 3)
