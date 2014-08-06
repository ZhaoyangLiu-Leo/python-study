import random
import math

print random.randint(0, 10)

print random.randrange(0, 10, 2)

#计算多项式
def compute(x):
    result = (-5) * (x ** 5) + 69 * (x ** 2) - 47
    return result

#根据现值计算终值
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * ((1 + rate_per_period) ** periods)

#计算正多边形的面积
def compute_area(n, s):
    area = (1 / 4.0) * n * (s ** 2) / math.tan(math.pi / n)
    return area

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)


print "$1000 at 2% compounded daily for 3 years yields $", future_value(500, .04, 10, 10)
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
    
polygon_area = compute_area(7, 3)

print 'polygon_area =', polygon_area

temp = compute(0)
print 'f(0) =',temp

temp = compute(1)
print 'f(1) =',temp

temp = compute(2)
print 'f(2) =',temp

temp = compute(3)
print 'f(3) =',temp

