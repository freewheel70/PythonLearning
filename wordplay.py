fin = open("words.txt")


# for i in range(10):
#    print fin.readline().strip()

# for line in fin:
# print line.strip()

def has_no_e(word):
    return 'e' in word


total = 0
num_of_no_e = 0
for line in fin:
    print line.strip()
    total += 1
    if (has_no_e(line)):
        num_of_no_e += 1

print "------------"
print "total " + str(total)
print "no e words number " + str(num_of_no_e)
print num_of_no_e * 1.0 / total
