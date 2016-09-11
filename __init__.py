import math

print 'Hello world';

message = "new message";
print type(message);
print message

print message*2

result = math.pow(2,5)
print result


def myfunction():
    print "A new function without parameters";

myfunction();
myfunction();
myfunction();

def myfuncWithParams(num1,num2):
    return  num1+num2

print myfuncWithParams(2,3)

def strategyPattern(strategy):
    return strategy(6,7)

print strategyPattern(myfuncWithParams)
