'''
Docstring for DSA.pattern1
*****
*****
*****
*****
*****
'''

n=5#no of lines
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,n+1,1):#printing star is responsible by j
        print("*",end='')
    print("")

#*****************************************************************************************
'''
11111
22222
33333
44444
55555
'''
n=5#no of lines
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,n+1,1):#printing star is responsible by j
        print(i,end='')
    print("")

#*****************************************************************************************
'''
12345
12345
12345
12345
12345
'''
n=5#no of lines
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,n+1,1):#printing star is responsible by j
        print(j,end='')
    print("")

#*****************************************************************************************
#cutting off the patterns
'''
*       1
**      2
***     3
****    4
*****   5
'''
n=5#no of lines
#if no of stars are increasing from top to down then generalized form i+/- something
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,n+1,1):#printing is responsible by j
        print(j,end='')
    print("")

#*****************************************************************************************
'''
if no of stars are increasing from top to down then generalized form i+/- something
Number of stars     Generalization(i+/- something)
1        2              1       1+1=2
2        3              2       2+1=3
3        4              3
4        5              4
5        6              5
LHS             ==          RHS 
If LHS and RHS values are equal then dont do i+/-
'''
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,i+1,1):#printing is responsible by j
        print("*",end='')
    print("")

#*****************************************************************************************
'''
Number of stars     Generalization(i+/- something) [i+(i-1)-odd sequence pattern]
1                     1       1(i)+0(i-1)=2
3                     2       2+1=3
5                     3       3+2=5
7                     4       4+3=7
9                     5       5+4=9

*
***
*****
*******
*********
'''
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,i+(i-1)+1,1):#printing is responsible by j
        print("*",end='')
    print("")

#*****************************************************************************************
'''
Number of stars     Generalization(i+/- something) [i+i-even sequence pattern]
2                     1       1(i)+0(i)=2
4                     2       2+1=3 
6                     3       3+2=5
8                     4       4+3=7
10                    5       5+4=9

**
****
******
********
**********
'''
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,i+i+1,1):#printing is responsible by j
        print("*",end='')
    print("")

#*****************************************************************************************
#Phase 2 pattern
'''
*****
****
***
**
*
When stars are decreasing then we need to write (n-i)+/-something bcz to make generalization in decreasing order
Number of stars     Generalization(i+/- something) 
5                     5-1 = 4 (n-i+1)  
4                     5-2 = 3     
3                     5-3 = 2    
2                     5-4 = 1   
1                     5-5 = 0    
'''
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,(n-i+1)+1,1):#printing is responsible by j
        print("*",end='')
    print("")

#*****************************************************************************************
'''
Number of stars     Generalization(i+/- something) =>Try to represent generaization interms of i
9                     5-1 = 4 (i+5)  =>(n-i)+(n-i)+1
7                     5-2 = 3 (i+4)   
5                     5-3 = 2 (i+3)  
3                     5-4 = 1   
1                     5-5 = 0   

********
******
****
**
'''
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,(n-i)+(n-i)+1+1,1):#printing is responsible by j
        print("*",end='')
    print("")

#*****************************************************************************************
'''
Number of stars     Generalization(i+/- something) 
10                    5-1 = 4+6=(4+2)  =>(n-i)+(n-i)+2
8                     5-2 = 3 (i+4)   
6                     5-3 = 2 (i+3)  
4                     5-4 = 1   
2                     5-5 = 0  
**********
********
******
****
**
'''
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,(n-i)+(n-i)+2+1,1):#printing is responsible by j
        print("*",end='')
    print("")

#summary
#every pattern comes from square
#increasing->(i+/-something)
#decreasing->(n-i+/- something)

#*****************************************************************************************
'''
    *
   **
  ***
 ****
*****
Recombination(logic separate for space and star) - 2 j loops(1-space,1-star)
Number of spaces     Generalization(i+/- something) - n-1
4                     4(n-i)=4
3                     3
2                     2
1                     1

Star                  Generalization
1                       1
2                       2
3                       3
4                       4
5                       5
'''
for i in range(1,n+1,1):#changing line is responsible by i
    for j in range(1,n-i+1,1):#printing is responsible by j
        print(" ",end='')
    for j in range(1,i+1,1):#printing is responsible by j
        print("*",end='')
    print("")

#*****************************************************************************************
'''
Number of spaces     Generalization(i+/- something) 
0                     1(i-1)
1                     2
2                     3
3                     4
4                     5

Stars                  Generalization
5                       (5-1=4+1=5)=4(n-i+1)
4                       3
3                       2
2                       1
1                       0

* * * *
  * * *
    * *
      *
'''

for i in range(1,n+1,1):
    for j in range(1,i-1+1,1):
        print(" ",end=" ")
    for j in range(1,n-i+1,1):
        print("*",end=" ")
    print(" ")

#*****************************************************************************************
    '''
    equilateral traingle
    
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

    '''
n=5
for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):
        print(" ",end=" ")
    for j in range(1,i+(i-1)+1,1):
        print("*",end=" ")
    print(" ")

'''

'''
n=5
for i in range(1,n+1,1):
    for j in range(1,i-1+1):
        print(" ",end=" ")
    for j in range(1,2*(n-i)+1+1):
        print("*",end=" ")
    print(" ")

n=5
for i in range(n,-1,1):
    for j in range(1,n-i+1,1):
        print(" ",end=" ")
    for j in range(1,i+(i-1)+1,1):
        print("*",end=" ")
    print(" ")


#*****************************************************************************************
'''
Wherever the number series breaks the pattern becomes breaks and consider them as separate patterns
*
**
***
****
*****
----------------break------------
****
***
**
*
'''
n=5
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print(" ")
for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):
        print("*",end=" ")
    print(" ")


#*****************************************************************************************

'''
square cut pattern design
*
**
***
****
*****

######Starting value set by i loop and change n same row in done by j loop
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

row wise change in i loop
'''
n=5
x=1 #starting element of the pattern
for i in range(1,n+1,1):
    x=i
    for j in range(1,i+1,1):
        print(x,end=" ")
    print(" ")


#*****************************************************************************************

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
column wise change in j loop
'''
n=5
x=1 #starting element of the pattern
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        x=j
        print(x,end=" ")
    print(" ")

n=5
x=1 #starting element of the pattern
for i in range(1,n+1,1):
    x=1
    for j in range(1,i+1,1):
        print(x,end=" ")
        x+=1
    print(" ")


#*****************************************************************************************

'''
#do not reset value of y in i loop in continous program
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
n=5
x=1 #starting element of the pattern
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(x,end=" ")
        x+=1 #value in row is increasing
    print(" ")


#*****************************************************************************************

'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
n=5
x=5 #starting element of the pattern
for i in range(1,n+1,1):
    x=5
    for j in range(1,i+1,1):
        print(x,end=" ")
        x-=1 #value in row is decreasing
    print(" ")


#*****************************************************************************************

'''
15
14 13
12 11 10
9 8 7 6
5 4 3 2 1
'''
n=5
x=15 #starting element of the pattern
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(x,end=" ")
        x-=1 #value in row is decreasing
    print(" ")


#*****************************************************************************************

'''
in numbers do not consider equilateral traingle
1.space + 2.left half + 3.right half

space
+

        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

+

1
2 1
3 2 1
4 3 2 1

=

        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''
x=1
for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):
        print(" ",end=" ")
    x=1
    for j in range(1,i+1,1):
        print(x,end=" ")
        x+=1
    x=i-1
    for j in range(1,i-1+1,1):
        print(x,end=" ")
        x-=1
    print(" ")

#*****************************************************************************************
'''
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''
for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):
        print(" ",end=" ")
    x=i
    for j in range(1,i+1,1):
        print(x,end=" ")
        x-=1
    for j in range(1,i-1+1,1):
        x=j+1
        print(x,end=" ")
        #x=2
        #print(x,end=" ")
        #x+=1
    print(" ")
#*****************************************************************************************
'''
1 1 1 1 1 1 1 1 1
1 2 2 2 2 2 2 2 1
1 2 3 3 3 3 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 4 4 3 2 1
1 2 3 3 3 3 3 2 1
1 2 2 2 2 2 2 2 1
1 1 1 1 1 1 1 1 1

'''
n=5
for i in range(1,n+1,1):
    x=1
    for j in range(1,i-1+1,1):
        print(x,end=" ")
        x+=1
    y=i
    for j in range(1,n-i+n-i+1+1,1):
        print(y,end=" ")
    z=i-1
    for j in range(1,i-1+1,1):
        print(z,end=" ")
        z-=1
    print(" ")
n=4
for i in range(1,n+1,1):
    y=1
    for j in range(1,n-i+1,1):
        print(y,end=" ")
        y+=1
    z=n-i+1
    for j in range(1,i+i+1+1,1):
        print(z,end=" ")
    z=n-i
    for j in range(1,n-i+1,1):
        print(z,end=" ")
        z-=1
    print(" ")