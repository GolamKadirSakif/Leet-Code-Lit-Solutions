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

        list_node=[] #stores k no. of nodes 
        first=True #flag to change the head of the linked list
        last_node=None #this saves the last node of the reversed k nodes
        current=head
        
        i=1 #keeps the count of the no. of elements processed and resets after processing k no. of nodes
        while current!=None:

            #Remember one important thing, here current node is the the k+1 node

            if i<=k:
                i+=1
                list_node.append(current)

                current=current.next
            elif i>k:
                i=2 #i here is reset to 2 and not 1 as in this instance the next node 1 is already processing. As you would notice i is always incremented to 1 greater than it's current node count 
                #Remember one important thing, here current node is the the k+1 node
                #Or the the next node to the k node

                for j in range(len(list_node)):
                    if j==0:#first member list
                        list_node[j].next=current #connecting the first node of the list to the current node
                        
                    elif j==(k-1): #last member of the list
                        if first==True:
                            head=list_node[j]

                        list_node[j].next=list_node[j-1]
                        if last_node!=None:
                            last_node.next=list_node[j]
                        

                    else:
                        list_node[j].next=list_node[j-1]
                

                first=False
                last_node=list_node[0] #this storing the last node of the reversed list, so that we can attach the later reversed list of nodes to the current list of nodes (linked list).
                list_node=[] #resetting the list after processing k no. of nodes
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
    BUT CAN BE USED TO TEST THE SOLUTION LOCALLY IN YOUR IDE.
     

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


lst = [1,2,3,4,5,6] # EDIT THIS TO MAKE YOUR DESIRED LINKED LIST  
linked_list_heads = list_to_linked_list(lst)



x=Solution()
z=x.reverseKGroup(linked_list_heads,2) #Change the number to change the position from where to reverse.

current=z
while current!=None:
    print(current.val)
    current=current.next





#I tried my best to explain my code if you need any help, dm.
# Caution: I am as confused as you are! hehe! 