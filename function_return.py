def calc_prod(lst):
    def prod():
        def prod_num(x,y):
            return x*y
        return reduce(prod_num,lst)
    return prod

f = calc_prod([1, 2, 3, 4])
print f()