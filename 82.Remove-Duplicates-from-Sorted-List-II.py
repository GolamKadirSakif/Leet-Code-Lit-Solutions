class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates( head):

    if head==None:
            return None

    i=head
    j=head.next
    temp=None
    
    flag=True
    
    while j!=None:
        if i.val!=j.val and flag==False:

            if temp==None:
                    head=j
                    i=j
                    j=j.next
                    flag=True
            else:
                    
                    temp.next=j
                    i=temp
                    flag=True


        elif i.val!=j.val:

            temp=i
            i=i.next
            j=j.next
            
        ####SAME#####
        elif i.val==j.val:
            if temp!=None:

                temp.next=None    
            j=j.next
            flag=False

    if flag==False and temp==None:
        return None


    return head




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



lst = [1,2,2]
linked_list_heads = list_to_linked_list(lst)


z=deleteDuplicates(linked_list_heads)

current=z
while current!=None:
    print(current.val)
    current=current.next

#Glad t's over!!
#Gotta work on making a better code for this problem
#Throughly understanding the concepts is very important