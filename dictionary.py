d = {'a':1, 'b':2, 'c':3}
balls = [[-5, 40], [20, 30], [-10, 40], [50, 60]]
l = [1, 2, 3, 4]

def is_in_range(ball):
    return ball[0] >= 0 and ball[1] >= 0

def balls_in_range():
    result = []
    for ball in balls:
        if is_in_range(ball):
            result.append(ball)
    return result

def balls_in_range2():
    return [ball for ball in balls if is_in_range(ball)]


def square():
    return [n ** 2 for n in l]


print d['a']
print balls_in_range()
print balls_in_range2()
print l
l = square()
print l
