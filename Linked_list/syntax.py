#Singly Linked Lists

class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
    
head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

head.next = A
A.next = B
B.next = C

print(head)

#traverse the list - O(n)
curr = head
while curr:
    print(curr)
    curr = curr.next

#displaying the linked list - O(n)
def display(head):
    curr= head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('->'.join(elements))

display(head)

#search for node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    
    return False
search(head, 7)


#doubly linked lists
class DoublyNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __string__(self):
        return str(self.val)
    
    def display(head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print('<->'.join(elements))
    
    display(head)


#insert at beginning - O(1)

def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next = head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, val = 3)
display(head)        

#insert at the end - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev = tail)
    tail.next = new_node
    return head, new_node
head, tail = insert_at_end(head, tail, 7)
display(head)

