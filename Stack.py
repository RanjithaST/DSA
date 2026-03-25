'''
Stack
Last in first out

0  1  2  3  4  5
10 20 30 40 50 80

80
50 
40
30
20
10

in python - Stack
list.append() -> to insert at last
list.pop() -> to remove last element
'''
a=[]
x=10
for i in range(10):
    if i<6:
        a.append(x)
        x=x+10
    else:
        a.pop()
    print(a)
'''
[10]
[10, 20]
[10, 20, 30]
[10, 20, 30, 40]
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 50]
[10, 20, 30, 40]
[10, 20, 30]
[10, 20]
'''
'''
valid parenthesis

( { [ -> open parenthesis push to stack
) } ] -> Check last most inserted bracket.if it is match then pop it off
If it is perfect valid parenthisi then stack becomes empty

'''

a=[1,2,3,4,5,6]
if len(a)>0:
    print(a[len(a)-1])
'''
 File "d:\DSA\DSA\Stack.py", line 50, in <module>
    print(a[len(a)-1])
          ~^^^^^^^^^^
IndexError: list index out of range

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in s:
            if i in ['(','[','{']:
                l.append(i)
            elif(len(l)!=0 and i==')' and l[len(l)-1]=='('):#last element
                l.pop()
            elif(len(l)!=0 and i==']' and l[len(l)-1]=='['):
                l.pop()
            elif(len(l)!=0 and i=='}' and l[len(l)-1]=='{'):
                l.pop()
            else:
                return False
        if len(l)==0:
            return True #if valid parenthesis stack will be empty
        return False #if everything is opening bracket
                

        
 '''
    
