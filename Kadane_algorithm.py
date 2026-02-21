# '''
# Kadane's algorithm: updated version of prefix sum
# previous sum + i(current no) is better or only i is better.
# which ever is better take that value

# Used to give,
# 1.Max sum sub array
# 2.Min sum sub array

# a=[10,20,-5,5,10,20,30]
# Here.max sum subarray is complete array sum: [10,20,-5,5,10,20,30]=95
# a=[10,20,-100,40,50,-100,20,10] - total array gives: -50 but 40,50 gives 90

# Steps:
# max=0 (stores max sum)
# a=[10,20,-5,0,-5,10,20,30,-10,50]
# sum=0
# totalSum=0 (sum from 0 to i position.Gives total sum of entitr array)
# '''
# '''
# sum=0
# max1=0
# psum=0
# a=[10,20,30,-500,10,15,10,8]
# for i in a:
#    max1=max(max1+i,i)
#    print(max1,end=" ")
# '''
# sum=0
# psum=0
# a=[10,20,30,-500,10,15,10,8]
# b=[]
# for i in a:
#    psum=psum+i
#    psum=max(psum,i)
#    b.append(psum)
#    print(psum,end=" ")
# print()
# print(max(b))


#or 
# max subarray
sum=0
psum=0
a=[10,20,30,-500,10,15,10,8]
submax=a[0] #if all array ele are negative then it will return 0 so never assign 0 to submax.
#Bcz the comparision should happen only between the elements present in array
for i in a:
   psum=psum+i
   psum=max(psum,i)
   print(psum,end=" ")
   submax=max(submax,psum)
print()
print(submax)


#min subarray - subarray whose sum is the smallest
sum=0
psum=0
a=[10,20,30,-500,10,15,10,8]
submin=a[0] #if all array ele are negative then it will return 0 so never assign 0 to submax.
#Bcz the comparision should happen only between the elements present in array
for i in a:
   psum=psum+i
   psum=min(psum,i)
   print(psum,end=" ")
   submin=min(submin,psum)
print()
print(submin)

#sum of all the negative values gives smallest subarray