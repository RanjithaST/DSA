'''
Docstring for DSA.Prefix_SumDS
Prefix sum data structure
comes in,
->hashing
->greedy
->DP

a=[10 20 30 40 50]
find the sum of elements upto ith index number
if i=0 then sum=10
if i=1 then sum=10+20=30 ..so on

a=[10,20,30,40,50]
prefix_sum=[10,30,60,100,150,210,280]
p[0]=0 to 0 index sum
p[1]=0 to 1 index sum ..so on
'''
a=[10,20,30,40,50]
psum=[0 for i in range(len(a))]
print(psum)

'''
sum=0 - (0+10=10)) -(20+10=30)
a=[10,20,30,40,50]
psum=[0,0,0,0,0]
for x in a:
    sum+=x
'''
total=0
for x in a:
    total+=x
    print(total,end=" ")

#*******************************************************************************

#Nested list/2D list - follows the concept of matrix
'''
    0 1 2
a[0[1,2,3]
  1[2,3,4]
  2[4 5 6]]
'''
#list within list
#Eg, [[1,2,3],[4,5,6],[1,2,3,4]] ->1 main list within that 2 sublists
a=[[1,2,3],[2,3,4],[5,6,7]]
print(a[0]) #[1, 2, 3]
print(a[0][0]) #1

'''for i in a:
    print(i)
    ###[1, 2, 3]
       [2, 3, 4]
       [5, 6, 7]'''
for i in a:
    print(i)#This will pick 1 list
    for j in i:#This will access each element of that list
        print(j)

#*******************************************************************************
'''
[1, 2, 3]
1
2
3
[2, 3, 4]
2
3
4
[5, 6, 7]
5
6
7
'''

#*******************************************************************************
#Accessing using index number
for i in range(len(a)):
    print(a[i])
    for j in range(len(a[i])):
        print(a[i][j])


'''
1 2 3
2 3 4
5 6 7
'''
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print(" ")

#*******************************************************************************
#Diagonal Difference
'''
         0 1 2
     0   1 2 3
     1   4 5 6
     2   9 8 9  
The left-to-right diagonal = 1+5+9=15 (i==j)
The right-to-left diagonal = 3+5+9=17 (i+j==n-1)#Generalize
Their absolute difference is=|15-17|=2
'''
a=[[1,2,3],[4,5,6],[9,8,9]]
sum1=0
sum2=0
n=len(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        if(i==j):
            sum1+=a[i][j]
        if(i+j==n-1):
            sum2+=a[i][j]
print(abs(sum1-sum2)) #Output is 2

#***************************************************************************
#min max sum
a=[1,2,3,4,5]
s=sum(a)
print(s-max(a),s-min(a))
#****************************************************************************


