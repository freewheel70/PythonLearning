def f(s):
    a = s.lower()
    t = list(a)
    t[0] = t[0].upper()
    return "".join(t)


print f("HELLo worLd")
print "HELLo worLd".capitalize()

def prod(x, y):
    return x*y


print reduce(prod, [2, 4, 5, 7, 12])
