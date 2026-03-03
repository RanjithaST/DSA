#Print true if there exist a subarray whose xor=0 else print false
#a=[--------[---subarray---]--------]
#            xor=0 means return true else false
'''
a b   a xor(^)b
0 0     0
0 1     1
1 0     1
1 1     0
'''
#a=[1,2,0,3,2,3,2,1,5,7]
# 1 - 0 0 1 xor 0 - 0 0 0 so 1^0 is 0 0 1
'''
1- 0 0 1
2- 0 1 0
ans - 0 1 1 =3

3^0=3
3^3=0
0^2=2
2^3=1
0 1 0
0 1 1
0 0 1

1^2=3
0 0 1
0 1 0

3^1=2
0 1 1
0 0 1
0 1 0

2^5=7
0 1 0
1 0 1
1 1 1

7^7=0

psum keys=[1 3 3 0 2 1 3 2 7 0]
psum[j]-psum[i]==  k
curr    old      constant

a^b==0
curr old fixed
old=fixed^curr
old= 0^curr=curr

curr = 31 and previous xor =31 then there will be subarray whose xor will be zero
31^31=0
'''
#a=[1,2,3,2,3,2,1,5,7]
#psum_keys(xor if i in a)=[1,3,0,2,1,3,2,7,0]
#if in hashmap same number repeats twice then xor is 0 [3,2,3,2,1,5,7] 7^7=0
#[1,2,3,2,3]=1^2=3^3=0^2=2^3=1 so 1 and 1 (first and last element is same then subarray will have )(0 in middle).
#if in hashmap if there repeats 2 same pxor values then that subarray will be zero

'''
[2 1 1 1 2 2 1 1 ]
pxor= [0 2 3 2 3 1 3 2 3]
[2(1st element excluded)        1  1  2 2 1 1] = 0 1 3 1 0
in hashmap (old xor sum)==curr xor the sub xor is 0
'''
a=[2 ,1, 1, 1, 2, 2, 1, 1 ]
h=dict()
xor=0
h[0]=1
mark=0
for i in a:
    xor=xor^i
    print(xor)
    if xor in h.keys():
        print("true")
        mark=1
    h[xor]=1
if mark==0:
    print("false")
print(h)