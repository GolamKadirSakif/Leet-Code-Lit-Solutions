# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None:
            return None
        


        i=head
        j=head.next
        flag=True

        while j!=None:
            if i.val==j.val:
                #i.next=None
                j=j.next
                flag=False

            elif i.val!=j.val and flag==False:
                i.next=None
                i.next=j
                i=i.next
                j=j.next
                flag=True


            elif i.val!=j.val:
                i=i.next
                j=j.next

        if flag==False and j==None:
            i.next=None


        return head