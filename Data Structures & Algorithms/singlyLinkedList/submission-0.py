class Node:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.val
            else:
                current = current.next
                i+= 1
        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val, self.head.next)
        self.head.next = new

        if not new.next:
            self.tail = new

    def insertTail(self, val: int) -> None:
        new = Node(val)
        self.tail.next = new
        self.tail = new

    def remove(self, index: int) -> bool:
        current = self.head
        i = 0
        while current and current.next:
            if i == index:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return True
            current = current.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
        return arr
