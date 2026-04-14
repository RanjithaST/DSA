'''
You are given an array in sorted array you need to 
find insertion position of the given element.return insertion position
'''
a=[10,20,30,40,50,70,80,100]
target=60
i=0
j=len(a)-1
while(i<j):
    if(target<a[i]):
        j=j-1
    elif(target>a[i]):
        i=i+1
    else:
        retir
if(j>=i):
    print(j)


