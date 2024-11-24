# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        ll = []
        cur = head
        while cur:
            ll.append(cur)
            cur = cur.next
        
        lft = 1
        rgt = len(ll)-1
        nxt = 1 # 1 if next is rgt
        cur = head
        while(lft <= rgt):
            next_node = ll[rgt] if nxt else ll[lft]
            cur.next = next_node
            cur = next_node
            if nxt:
                rgt -= 1
            else:
                lft += 1
            nxt = not nxt
        
        cur.next = None

