'''
Array(static size) collection of elements of same datatypes is called as array

Python: List
-collections
-different types of elements
-size is dynamic(we can increase and decrease however we need as per requirement)
Example:
#a=[1,2,3,4,5] index-0,1,2,3,4

Methods
1.append-a.append(10)
2.fetch-a[0]
3.update-a[0]=1
4.pop-a.pop(1)
'''
a=[]
print(a)
#append is used to add element to array
a.append(1)
a.append(10.0)
a.append("Ram")
print(a)
#fetching by index
print(a[0])
#update value of 1 index
a[0]=12
print(a[0])
a.pop(0)
print(a)

#******************************************************************
'''
1.Finding largest element
->All elements should be of same type
'''
a=[]
a.append(10)
a.append(20)
a.append(300)
a.append(4)
print(a)
print(max(a))

max1=a[0]
for x in a:
    if x>max1:
        max1=x
print(max1)


#******************************************************************
'''
2.Finding minimun element in array
'''
print(min(a))

min1=a[0]
for x in a:
    if x<max1:
        min1=x
print(min1)

#******************************************************************
'''
Find whether element is present or not in an array(Search)
'''
if 10 in a:
    print("True")
else:
    print("False")


#******************************************************************
'''
Sort - ascending
'''
print(a)
a.sort()
print(a)
#******************************************************************
'''
Sort-descending
'''
print(a)
a.sort(reverse=True)
print(a)
a.sort()
a=a[::-1]
print(a)
#******************************************************************
'''
Accessing elements of loop
'''
a=[1,2,3,4,5]
#direct
for x in a:
    print(x)
#using index
for i in range(len(a)):
    print(a[i])

