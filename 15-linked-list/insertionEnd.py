class Node:
    def __init__(self,value):
        self.key = value
        self.next = None
        
n1 = Node(0)
n2 = Node(1)
n3 = Node(2)

head = n1
n1.next = n2
n2.next = n3

def printList(head: Node):
    "traverse through a linked list and print its values"
    curr = head
    while(curr != None):
        print(curr.key,end=" ")
        # get the next value of current node.
        curr = curr.next
    

# a function to do the above task
def insertionAtEnd(node: Node, val: int,prevHead: head) -> Node:
    "insert a node at the end of a the linked list"
    # do not update head, always keep a pointer to it.
    temp = prevHead
    # until you did not hit None value for temp.next, it means have not reached to the end of the linked list.
    while(temp.next != None):
        # assign the next value to temp.
        temp = temp.next
    # change the structure of the linked list and add value to its key.
    temp.next = node(val)
    printList(prevHead)
    

insertionAtEnd(node = Node, val=9,prevHead = head )

print()
printList(head)