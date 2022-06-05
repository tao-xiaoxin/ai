class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    prehead = ListNode(-1)

    prev = prehead
    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    prev.next = list1 if list1 is not None else list2

    return prehead.next


list1 = ListNode(1, ListNode(8, ListNode(11)))
list2 = ListNode(3, ListNode(4, ListNode(5)))

re = merge_two_lists(list1, list2)

while re:
    print(re.val)
    re = re.next
