#Binary search: works only on sorted array
#works on 2 pointers and array must be sorted whenever we take 2 pointers
'''
[a b c d e f g h i j k l m n o p]
 l++                           r--
 array is strictly incrasing and find a[l]+a[r]==target
 if a[l]+a[r]>target: then decrement right,if we increment left again it becomes more than target
 l pointer -> sum increases
 r pointer -> sum decreases
 a[l]+a[r]<target: increment left pointer.
 a[l]+a[r]>target: decrement right pointer.
 until(l<r) we need to increment and decrease
'''