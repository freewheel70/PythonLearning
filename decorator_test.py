import time

def performance(f):
    def fn(*args,**kwargs):
        start = int(round(time.time() * 1000))
        result = f(*args,**kwargs)
        end = int(round(time.time() * 1000))
        print "call "+f.__name__ + "() in "+ str(end-start)+" milliseconds"
        return result
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)