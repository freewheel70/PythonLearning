def count():
    fs = []
    for i in range(1, 4):
        def f(m=i):
            return m*m
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()


# 方法：问题的产生是因为函数只在执行时才去获取外层参数i，若函数定义时可以获取到i，问题便可解决。
# 而默认参数正好可以完成定义时获取i值且运行函数时无需参数输入的功能，所以在函数f()定义中改为f(m = i),
# 函数f返回值改为m*m即可.