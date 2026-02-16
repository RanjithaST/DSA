#HashMap: Frequency array
'''
Hashmap is a unique Data Structure which comprises of 2 values(combination of key and value pair)
1.Key-Features:Key must have datatype and key are unique(no 2 key can have same value)
eg:{1,2,1}-not allowed ,{1,2,3}-allowed
2.values:values can be duplicated
<key,value>
<Anything,Anything>

Python-HashMap=Dictionary
'''

h={}
#Insertion into hashmap (using index no for python)
#if key doesnt exist then java gives null but python gives error
h[1]="Pavan" 
print(h)
h[2]="Pavan"
print(h)
h[1]="Garishma" #if same key again then key will get updated
print(h)
h[3]="Dell"
h[4]="lenova"
h[5]="mac"

#need to see only keys using keys() method
print(h.keys())
#need to see all values using values() method
print(h.values())
#need to see both keys and values
print(h)
#check if key (set datastructure) is present in hashmap 
print(1 in h.keys())
#check if value is present in hashmap 
print(1 in h.values())

#iterating hashmap using loops
'''
It is possible to iterate the hashmap using keys
'''

for i in h.keys():
    print(i)#key
    print(h[i])#value

#`. Write  a program to create frequency hashmap
'''
Write a python program to print occurance of given number in array 
or all the numbers in an array
For occurance select hashmap data structure

Frequency hashmap format:
h={
<key,value>
<number,how many times it has come>

a=[10,20,10,20,30,40,50,10,10,10,20,30,40,50]
<10,5>
<20,3>
<30,2>
<40,2>
<50,2>
}


'''
a=[10,20,10,20,30,40,50,10,10,10,20,30,40,50]
h={}
for i in a:
    #case 1:what if key is already present
    #case 2:what if it is a new entry
    if(i in h.keys()):
        count=h[i]
        count=count+1
        h[i]=count
    else:
        h[i]=1
print(h[10])
