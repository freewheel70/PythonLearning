print "abc">"bcd"

print "abc">"acd"
print "abc">"Acd"

#"avd".lower()


def cmp_ignore_case(s1, s2):
    result =  cmp(s1.lower(), s2.lower())
    print s1+" "+s2+" "+str(result)
    return result

print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


