'''
Anagram : same alphabets but order may change

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h=dict()
        h1=dict()
        for char in s:
            if char in h:
                count=h[char]
                count=count+1
                h[char]=count
            else:
                h[char]=1
        for char in t:
            if char in h1:
                count=h1[char]
                count=count+1
                h1[char]=count
            else:
                h1[char]=1
        if(len(h)!=len(h1)):#key count not same
            return False
        for i in h.keys():
            if i not in h1.keys():#key difference
                return False
            elif h[i]!=h1[i]:#count of value is difference
                return False
        return True
    

#or

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
#or
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h=dict()
        h1=dict()
        for char in s:
            if char in h:
                count=h[char]
                count=count+1
                h[char]=count
            else:
                h[char]=1
        for char in t:
            if char in h1:
                count=h1[char]
                count=count+1
                h1[char]=count
            else:
                h1[char]=1
        if h==h1:
            return True
        else:
            return False

#or
'''
# s='dog'
# t='godd'
# s1=list(s)
# t1=list(t)
# if s1.sort()==t1.sort(): Not works bcz it returns NULL
#     print("Anagram")
# else:
#     print("Not anagram")

#Sorting method to check anagram
s='dogd'
t='godd'
s1=list(s)
t1=list(t)
s1.sort()
t1.sort()
if s1==t1:
    print("Anagram")
else:
    print("Not anagram")
