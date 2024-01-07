class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None  # prev, data, next = None

    def print_forward(self):
        if self.head is None:
            raise Exception("The linked list is empty")

        current_node = self.head
        ll_str = 'Head --> ' + str(self.head.data)
        while current_node:
            ll_str += ' --> ' + str(current_node.next.data) if current_node.next else ' --> None '
            current_node = current_node.next
        print("Linked List:", ll_str)

    def print_backward(self):
        if self.head is None:
            raise Exception("The linked list is empty")
        current_node = self.head
        ll_str = "Head <-- "
        while current_node:
            if current_node.next:
                ll_str += str(current_node.data) + ' <-- '
            else:
                ll_str += str(current_node.data) + ' <-- None '
            current_node = current_node.next
        print("Link list in reverse: ", ll_str)

    def get_last_node(self):
        if self.head is None:
            raise Exception("The list is empty!!")
        current_node = self.head
        while current_node:
            if current_node.next is None:
                return current_node
            current_node = current_node.next

    def get_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return
        new_node = Node(None, data, next=self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return
        current_node = self.head
        while current_node:
            if not current_node.next:
                new_node = Node(current_node, data, next=None)
                current_node.next = new_node
                return
            current_node = current_node.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index had been given !!")
        if index == 0:
            new_node = Node(None, data, next=self.head)
            self.head = new_node
            return
        curr_ind = 0
        curr_node = self.head
        while curr_node:
            if curr_ind == index - 1:
                new_node = Node(prev=curr_node, data=data, next=curr_node.next)
                curr_node.next = new_node
                return
            curr_node = curr_node.next
            curr_ind += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index had been given !!")
        if self.head is None:
            raise Exception("The list is empty !!")
        curr_ind = 0
        curr_node = self.head
        while curr_node:
            if curr_ind == index - 1:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()
