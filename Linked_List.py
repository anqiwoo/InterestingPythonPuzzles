import random


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


random.seed(0)
linked_list = LinkedList()
for _ in range(10):
    linked_list.append(Element(random.gauss(0, 1)))

print(linked_list.head.value)
