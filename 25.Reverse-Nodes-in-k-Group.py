# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]

        """

        list_node=[]
        first=True
        current=head
        last_node=None
        i=1
        while current!=None:
            

            if i<=k:
                i+=1
                list_node.append(current)

                current=current.next
            elif i>k:
                i=2
                for j in range(len(list_node)):
                    if j==0:#first member
                        list_node[j].next=current
                        
                    elif j==(k-1): #last member of the list
                        if first==True:
                            head=list_node[j]

                        list_node[j].next=list_node[j-1]
                        if last_node!=None:
                            last_node.next=list_node[j]
                        

                    else:
                        list_node[j].next=list_node[j-1]
                

                first=False
                last_node=list_node[0]
                list_node=[]
                list_node.append(current)
                current=current.next


        if len(list_node)==k and current==None:
                i=2
                for j in range(len(list_node)):
                    if j==0:#first member
                        list_node[j].next=None
                        
                    elif j==(k-1): #last member of the list
                        if first==True:
                            head=list_node[j]

                        list_node[j].next=list_node[j-1]
                        if last_node!=None:
                            last_node.next=list_node[j]
                        

                    else:
                        list_node[j].next=list_node[j-1]

        return head
 


"""""
    THE FOLLOWING PART IS NOT PART OF THE SOLUTION.
    BUT CAN BE USED TO TEST THE SOLUTION LOCALLY
     

"""""




def list_to_linked_list(lst):
    """Convert a Python list into a linked list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


lst = [1,2,3,4,5,6]
linked_list_heads = list_to_linked_list(lst)



x=Solution()
z=x.reverseKGroup(linked_list_heads,2)

current=z
while current!=None:
    print(current.val)
    current=current.next