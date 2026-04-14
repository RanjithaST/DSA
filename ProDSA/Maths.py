'''
4 chapters
*********************************************************************
1.factors
2.successive calculation
3.genesis and destruction of a number
4.amstrong number

Maths:
1.Arithmatic op set
= - * / // ** % (7 is python)
+ - * / % (5 in python)
+ - * / % ** (6 in javascript parseInt(a/b)=> similar to // in python)
2.Bitwise op set


1. Factors
a is said to be a factor of b if b%a==0
a=2
b=10
a%b==0 so a is the factor of b
'''
'''
a=10
b=100
if b%a==0:
    print("a is the factor of b")

n=10
#a=[1,2,3,4,5,6,7,8,9,10] #posible factors
#print all the positive factors of the given no
for i in range(1,n+1):
    if n%i==0:
        print(i)
'''

'''
Successive calculations
1+2+3+..........+n
1*2*3*..........*n
we can use this operations only when all operators are same

identity element
sum=0
div=0
multi=1
div=1
'''
n=10
s=0
for i in range(1,n+1):
    s=s+i
print(s)