'''
Docstring for Hashmap2
HashMap variation 1:<number,not need>
HashMap Variation 2:<index,sum upto index>
Eg:
a=[10,20,30,40,50,60,70]
   1   2  3  4  5  6  7
{0,0}       <sum,upto index>
{10,1}
{30,2}
{60,3}
.
.
.
{280,7}
'''

#Prefix sum using HashMap
a=[10,20,30,40,50,60,70,80]
#index number starts from 1 to n
h={}
#h[0]=0 for subarray
sum=0
i=1
for x in a:
    sum=sum+x
    h[i]=sum #h[sum]=i we cant use because sum can be duplicated but index cant be duplicated
    i=i+1
print(a)
print(h)
print(h[2])#sum upto certain index

#print true if there is a subarray(apart of main array any number taken continously) sum==k else false
#we use prefix sum hashmap 
#O(n^3)--->O(n)
a=[10,20,30,40,10,20,30,10]
psum=[10,30,60,100,110,130,160,170]
k=70#target
'''
2 types of psum
<index,psum>
<psum,count>
'''
i=1
sum=0
h={}
h[0]=0 #bcz if [10,10,10,10,10] and k=50,50 will be skipped as 0 is not is h.so add h
mark=0
for x in a:
    sum=sum+x #curr prefix sum - old prefix sum==k so old=curr sum-k
    if(sum-k in h.values()):
        print("Yes")
        mark=1
    else:
        h[i]=sum
        i=i+1
if mark==0:
    print("No")

    

