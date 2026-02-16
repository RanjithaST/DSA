#Python datatypes - Dynamic in nature
'''
No limit for size in datatypes in python
Docstring for Datatypes

1.Numeric: deal with nos

a.Integer -whole no without fraction.eg:10,-10(can perform arithmetic and bitwise op)
b.Float-eg:12.21(can perform arithmatic operations)
c.Complex - real + imaginary part(can perform arithmaic operations)-eg:12+5j

2.Boolean

3.Set

4.Sequence 
a.Strings
b.List
c.Tuple
'''

#Numeric
a=2.1
print(type(a))
a=-10
print(type(a))
b=2+5j
c=3+7j
print(b+c)

#Sequence

#string
a="hirey"
print(type(a))
a="10"
b="20"
print(a+b)

#list=array of elements of different datatype->[]->Ordered and mutable
a=[]
print(type(a))
a=[1,2,3,'Hi']
print(a)

#List operations:
#append-attach to end
b=[]
b.append(1)
b.append('10')
b.append('Ram')
print(b)
#accessing using index(0-n)
print(a[1])
#insert in between or update the element of particular index
b.insert(1,'Hi')
print(b)
print(a[0])
a[0]=10
print(a[0])
a.extend([60, 70])  # add multiple
#Delete
a.remove(70)   # removes value
#pop()
a.pop()
print(a)
a.append(3)
print(a)
a.pop()
print(a)
#pop(index)
a.pop(1)
print(a)
#del a#delete variable

# len(a)
# max(a)
# min(a)
# sum(a)
# a.sort()
# a.reverse()
# a.count(10)
# a.index(30)


#2.tuple()-collection of elements of different datatype and immutable and ordered.
# once created cant be modified
c=(1,2,3)
print(type(c))
print(c[0])    # 1
print(c[-1])   #3
print(c[1:3])   # (2, 3)
c.count(1)
c.index(1)
len(c)
max(c)
min(c)
sum(c)

#set and dict use {}. type of {} is dict
#set - no duplication is allowed (bcz in set theory no duplication allowed) and
#  unordered and always sorted and can be modified and collection of different datatypes

'''
{}-dict
{1,2,3}-set
{1:'one',2:'three'}-dict
'''

a={1,2,3,1,0,'pavan'}#{0, 1, 2, 3, 'pavan'}
print(a)
'''
s.remove(3)    # removes 3 (error if not present)
s.discard(10)  # no error even if not present
s.pop()        # removes random element
s.clear()      # removes all elements
'''


#dictionary - No duplication,key-value pair
#a={key:value} key value is used as index and key value can be of any datatype
a={1:'one',2:'two',0:'zero','three':3}
print(a)

#boolean
a=True #True means 1 else 0
type(a)
print(a)

d=None#if we need to use d variable sometime but u dont know.None is used to preseve variable
#with no datatype




