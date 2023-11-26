class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("[]")
        else:
            node = self.head
            result = ''
            while node is not None:
                result = result + str(node.data) + ', '
                node = node.next_node
            result = result[:-2]
            print("[" + result + "]")

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node

    def search(self, data):
        if self.head is None:
            return 0
        else:
            position = 1
            node = self.head
            while node:
                if node.data == data:
                    return position
                node = node.next_node
                position += 1
            return 0

    def delete(self, data):
        if self.head is None:
            return 0
        else:

            position = 1
            previous = None

            if self.head.data == data:
                self.head = self.head.next_node
                return position

            node = self.head
            while node:
                if node.data == data:
                    previous.next_node = node.next_node
                    return position
                node = node.next_node
                position += 1
            return 0

    def add_at_start(self, data):
        if self.head is None:
            return 0
        
        pass


    def add_at_pos(self, data, pos):
        pass

    def reverse(self, linklist):
        pass


link_list = LinkedList()
link_list.print()
link_list.add(6)
link_list.add(11)
link_list.add(12)
link_list.print()
link_list.add(7)
link_list.print()
# print(link_list.search(7))
# print(link_list.search(6))
# print(link_list.search(100))
# print(link_list.delete())
p = link_list.delete(6)
print(p)
link_list.delete(12)
print(p)


# special add at beginning
# add at particular position
