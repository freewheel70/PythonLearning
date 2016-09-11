def sum(result,num):
    if num == 1:
        return result+num;
    else:
        return sum(result+num,num-1)

def sumUp(num):
    return sum(0,num)

num = int(raw_input("sum up to ?"))
print sumUp(num)