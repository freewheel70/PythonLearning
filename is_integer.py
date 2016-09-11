def isInteger(a):
    return isinstance(a,int)

print isInteger(2.0)
print isInteger(2)
print isInteger("2")

import math

def is_sqr(x):
    result = math.sqrt(x).is_integer()
    print str(x)+" "+str(result)
    return result

print filter(is_sqr, range(1, 101))