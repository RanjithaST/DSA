a=[1,3,2,1]
n=4
for i in range(1,n-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        print(a[i])
    