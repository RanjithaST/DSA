# n=5#no of lines
# #if no of stars are increasing from top to down then generalized form i+/- something
# for i in range(1,n+1,1):#changing line is responsible by i
#     for j in range(1,n+1,1):#printing is responsible by j
#         print(j,end='')
#     print("")

n=4
size=n*2-1
for i in range(1,size+1):
    for j in range(1,size+1):
        if(i==1 or j==1 or i==size or j==size):
            print(n,end=" ")
        elif(i==2 or j==2 or i==size-1 or j==size-1):
            print(n-1,end=" ")
        elif(i==3 or j==3 or i==size-2 or j==size-2):
            print(n-2,end=" ")
        elif(i==4 or j==4 or i==size-3 or j==size-3):
            print(n-3,end=" ")
    print(" ")
        