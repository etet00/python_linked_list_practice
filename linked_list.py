# linked_list practice

def main():
    linked_list = Linked_list()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(7)
    # linked_list.add(9)
    linked_list.print()

class Node:
    def __init__(self, data = None, next = None):
        self.value = data
        self.next = next

class Linked_list:
    def __init__(self, start_node = None, end_node = None):
        self.start_node = start_node
        self.end_node = end_node

    def add(self, input_data):
        new_node = Node(input_data)
        if self.start_node == None:
            self.start_node = new_node
            self.end_node = new_node
        else:
            # print(self.end_node.next)
            self.end_node.next = new_node
            # print(self.end_node.next.value)
            self.end_node = self.end_node.next
            # print(self.end_node.value)


    def print(self):
        node = self.start_node
        while node:
            print(node.value)
            node = node.next

if __name__ == "__main__":
    main()
