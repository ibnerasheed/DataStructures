class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# without oops


def add(data, head):
    temp = head
    newNode = Node(data)
    if temp is None:
        temp = newNode
        return temp
    else:
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        return head


def show(head):
    if head is None:
        print("Empty")
    else:
        while head != None:
            print(head.data)
            head = head.next
    print("...........................")


head = None
show(head)
head = add(4, head)
show(head)

head = add(5, head)
show(head)
head = add(11, head)
show(head)
head = add(17, head)
show(head)
