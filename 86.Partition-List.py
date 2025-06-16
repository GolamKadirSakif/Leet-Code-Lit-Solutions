class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def partition(head, x):
        

        lsn=None
        prev=None
        current=head

        while current!=None:
            next=current.next
            if current.val<x and current==head:# if the starting val is smaller
                lsn=current
                prev=current
                current=next

            elif current.val<x and lsn==None: #when the list does not start with the lower value 
                lsn=current
                prev.next=None
                prev.next=current.next
                
                current.next=None
                current.next=head
                head=current

                prev=prev
                current=next

            elif current.val<x and lsn==prev:
                lsn=current
                prev=current
                current=next
            elif current.val<x: #in the middle of the list
                    
                current.next=None
                current.next=lsn.next

                lsn.next=None
                lsn.next=current


                lsn=current

                prev.next=None
                prev.next=next

                prev=prev
                current=next
            
            

            
            else:

                prev=current
                current=next

        return head         















#tester code #Not part of the solution

def list_to_linked_list(arr):
    """Convert a NumPy array (or list) into a linked list."""
    if arr is None or len(arr) == 0:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



lst = [3,1,2]
linked_list_heads = list_to_linked_list(lst)


z=partition(linked_list_heads,3)

current=z
while current!=None:
    print(current.val)
    current=current.next