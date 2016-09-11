aString = "abcdefg"
print aString
print aString[1]
print len(aString)
print "-----------"
for ch in aString:
    print ch

print aString[2:6]
print aString[:6]
print aString[2:]

print aString.find("d")

print aString.upper()

print ("a" in aString)
print ("az" in aString)