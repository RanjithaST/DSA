'''
Docstring for Strings
Strings - collection of characters

Methods:
1.len() - considers space as well
2.access - using for(only in python in java we need to break string into array of characters)

'''
p="Ranjitha"
print(len(p))
for i in p:
    print(i)

'''
Frequency hashmap for string - counting no of characters
'''
h={}
for i in p:
    if i in h:
        count=h[i]
        count=count+1
        h[i]=count
    else:
        h[i]=1
print(h)


