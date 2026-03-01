#Print longest subarray and its length where end of subarrays having the same element at first and last.

a=[10,2,5,6,2,11,6,5,10,2]
'''
valid subarrays:
10,2,5,6,2,11,6,5,10
2,5,6,2,11,6,5,10,2
2,11,6,5,10,2
2,5,6,2
6,2,11,6

a=[* * 10 * * * * 10 * * * * 10]
   0 1  3 4 5 6 7 8  9  10 ...13
   2-13 is longest
longest subarray - 2 to till end
longest subarray- first entry is permanent entry,remaining entries is for calculation
# Generally we take index no 1
'''
a=[10,2,5,6,2,11,10,6,5,10,2] #0 based indexing
h={} #key is number and value is 1st occurance of the index of the number
i=1
for x in a:
    if x in h: #only first occurance so pass
        start=h[x] #first element
        end=i
        #0 based indexing so reduce start and end by 1
        start=start-1
        end=end-1
        #print(a[start:end+1])  or
        for j in range(start,end+1,1):
             print(a[j],end=" ")
        print(" ")
    else:
        h[x]=i
    i+=1
print(h) #{10: 1, 2: 2, 5: 3, 6: 4, 11: 6}

#above program print all subarray from i to i.
#below is the program to print longest subarray with starting and ending value is same
'''
a=[10 ------------------------------------------------------------------10]
  mark1        maxlen=size of longest subarray(distance)              mark2
'''
a=[10,2,5,6,2,11,10,6,5,10,2] #0 based indexing
h={} #key is number and value is 1st occurance of the index of the number
mark1=0
mark2=0
maxlen=0
i=1
for x in a:
    if x in h and i-h[x]>maxlen: #only first occurance so pass
        maxlen=i-h[x] #4-1=3 eventhough length is 4(4 elements are there so add 1)
        mark1=h[x]
        mark2=i
    else:
        h[x]=i
    i+=1
print(h) #{10: 1, 2: 2, 5: 3, 6: 4, 11: 6}
print(a[mark1-1:mark2-1+1])
mark1=mark1-1
mark2=mark2-1
for j in range(mark1,mark2+1):
    print(a[j],end=" ")
print(" ")#for space
print(maxlen+1)#maxlen will always have 1 value less(Both in 0 and 1 based indexing)