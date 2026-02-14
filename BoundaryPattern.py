#selecion of i and j should be done for printing the star.select to print only when there is required
'''
Docstring for DSA.BoundaryPattern
*  *  *  *  *  *  *  *  *   
*                       *   
*                       *
*                       *
*                       *
*                       *
*                       *
*                       *
*  *  *  *  *  *  *  *  *
use if and else inside j loop
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==1 or i==n or j==1 or j==n):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")
'''
Normal diagonal-starts from left and goes to the right
Row no=Column no
*  *  *  *  *  *  *  *  * i==1
*  *  (1==1)            *
*     *  (2==2)         *
*        *              *
*           *           *
*              *        *
*                 *     *
*                    *  *
*  *  *  *  *  *  *  *  * i==n
j==1                    j==n
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==1 or i==n or j==1 or j==n or i==j):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")

'''
Cross diagonal-common sum diagonal:right to left
*  *  *  *  *  *  *  *  *(1,9)
*                    * (2,8) *
*                 *(3,7)   *
*              *(4,6)      *
*           *           *
*        *              *
*     *                 *
*  *                    *
*  *  *  *  *  *  *  *  *
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==1 or i==n or j==1 or j==n or i+j==n+1):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")
'''
*(i==j)                 *(i+j==n)
   *                 *
      *           *
         *     *
            *
         *     *
      *           *
   *                 *
*                       *
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==j or i+j==n+1):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")

'''
*
*  *
*     *
*        *
*           *
*              *
*                 *
*                    *
*  *  *  *  *  *  *  *  *
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==j or j==1 or i==n):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")

'''
* * * * * * * * *
*             *
*           *
*         *
*       *
*     *
*   *
* *
*
'''
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==1 or j==1 or i+j==n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

'''
 *  
              * *  
            *   *  
          *     *  
        *       *  
      *         *  
    *           *  
  *             *  
* * * * * * * * *  

'''
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(j==n or i==n or i+j==n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

'''
* * * * * * * * *
  *           *
    *       *
      *   *
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==1 or i==n or i+j==n+1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

'''
*               *
* *           * *
*   *       *   *
*     *   *     *
*       *       *
*     *   *     *
*   *       *   *
* *           * *
*               *
'''
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(j==1 or j==n or i+j==n+1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

'''
Diamond pattern

        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *

Generalization

cross
i+j  ==  n+1-4
1+5(6) ==10-4
2+4(6)==10-4
3+3
4+2
5+!

i==j+4(LHS==RHS)
5   1
6   2
7   3
8   4
9   5

1   5-4=1
2   6
3   7
4   8
5   9

cross
5+9(14)   n+1=10=n+1+4
6+8
7+7
8+6
9+5
'''
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i+j==n+1-4 or i==j+4 or i==j-4 or i+j==n+1+4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''
n=9
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i==n or i+j==n+1-4 or i==j-4):
            print("* ", end="")
        else:
            print("  ", end="")
    print()
'''


