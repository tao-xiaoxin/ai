class Node:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        headNext = self.head.next
        newNode = Node(value)
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = headNext
        headNext.prev = newNode
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        tailPrev = self.tail.prev
        newNode = Node(value)
        tailPrev.next = newNode
        newNode.prev = tailPrev
        newNode.next = self.tail
        self.tail.prev = newNode
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # 有趣的删除节点操作
        # 被删除的节点虽然保持着对next节点的引用 但是不用担心 因为没有了对被删除节点的引用 会被GC
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity