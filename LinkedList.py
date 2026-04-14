'''
Linked list:
chain ->segment(node)
[]-->[]-->[]-->[]
each node contains 2 parts: data and adsress
[data|address]
[value|connector]
chain where one segment connected to other segment

ListNode contanins {value and next=>datatype of next is listnode itself}
ListNode{
        int:value
        Listnode next=null}
 
 Address:       1000                2000
First node: [ 10  |  null ]       [20| null]

 Address:     head:1000            2000            3000
First node: [ 10  | 2000 ]------>[20| 3000]------>[15|null]
In single line array,last node points to null
                10-->20-->15-->null
                1000-->2000-->3000-->null
    after 3000 it bcmz null
while(head!=null):
    head=head.next
break out of loop when head bcmz null

In linked list value can be duplicated
adress is not duplicated
1000->2000->3000->4000->2000   --->This becomes cycle
10     20   30    40    20      30    40    20   30  20  .........

head=start
while(head!=null):
    head.val
    head=head.next
'''
'''
Middle=length/2
5/2=2+1=3 position need to be reached
4/2=2+1=3 position
min=len(a)/2

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=head
        length=0
        while(head!=None):
            length=length+1
            head=head.next
        length=length/2+1
        head=l
        count=0
        while(head!=None):
            count=count+1
            if(count==length):
                return head
            head=head.next
        
'''