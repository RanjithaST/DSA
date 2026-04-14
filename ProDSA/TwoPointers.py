'''
a=[1,2,3,4,5,6]
  0          6-1=5
while(i<j):
    #logic
    i++
    j--

cases/algorithm used

1.Sliding window
2.sub array
3.2sum,3sum,4sum
4.searching in sorted array : Binary search(log2(n)),Ternary serch-Fastest saerching in 
sorted array(log3(n))

2 cases:
1.if array is odd sized
2.array is even sized

2.array is even sized
a=[1,2,3,4]
   i     j
   i<j
   1<4 - T
   2<3 - T
   now
   3<2 - F
   
   if i<j and array is even sized means i!=j
   i and j will always point to 2 meadians of the array

1.if array is odd sized
a=[1,2,3,4,5]
   i   i   j
       j
i<j - 1<5 - T
      2<4 - T
      3<3 - False
      1.i<j break then i==j after 1st termination
      2.both i and j point to perfect median

      
        nums3=nums1+nums2
        nums3.sort()
        i=0
        j=len(nums3)-1
        while(i<j):
            i=i+1
            j=j-1
        if(i==j):
            return nums3[i]*1.0
        else:
            x=nums3[i]+nums3[j]
            x=x*1.0/2
            return x
'''

'''
Searching in sorted array
a=[1,2,3,4,5,  6,  7,10,30,90,100]
   i                           j
   0           5               11  

Two pointers + mid calculation = Binary search
'''
a=[1,2,3,4, 5, 6,7,10,30,90,100]
i=0
j=len(a)-1
x=10
while(i<=j):
    mid=int(i+(j-i)/2) #=> 11-0=11, 11/2=5 => 5+0=5   | (i+j)/2 if i==num j==num(if large num is there value crosses limit so subtract it)
    if(x==a[mid]):
        print("Got")
        print(mid)
    if(x>=a[mid]):
        i=mid+1 #6,[7,10,30,90,100]
    else:
        j=mid-1 #[1,2,3,4,5,],6 

'''
mid=5==>6
10>6
so,i=5+1=6
mid=11-6=5//2=2+6=8 ==>30
10<30
so,j=mid-1=7
mid=7-6=1//2=0+1=1+6=7 ==>10 found

'''

    
'''
Pair sum
a=[10 20 30 40 50 60  70]
    0                 len(a)-1


a[i]+a[j]=10+70=80
i++
20+70=90
i++
30+70=100
i++ j constant => sum increases

10+70=80
j--
10+60=70
j--
j-- i constant =>sum decreases
'''

