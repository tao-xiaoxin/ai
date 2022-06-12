from typing import List

class ListNode:
    def __init__(self,val=0,next=None):
        if isinstance(val,int):
            self.val = val
            self.next = next
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            head = self
            for i in val[1:]:
                node = ListNode(i,None)
                head.next = node
                head = head.next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def mergeTwoLists(a: ListNode, b: ListNode):
            merge = ListNode(-1)
            head = merge
            while a and b:
                if a.val > b.val:
                    head.next = b
                    b = b.next
                else:
                    head.next = a
                    a = a.next
                head = head.next
            head.next = a if a else b
            return merge.next

        if len(lists) == 0:
            return None
        res = None
        for i in range(0,len(lists)):
            res = mergeTwoLists(res,lists[i])
        return res



lists = [[1,4,5],[1,3,4],[2,6]]
l_nodes = []
for l in lists:
    listnode = ListNode(l)
    l_nodes.append(listnode)


solution = Solution()
merge = solution.mergeKLists(l_nodes)
while merge:
    print(merge.val)
    merge = merge.next
