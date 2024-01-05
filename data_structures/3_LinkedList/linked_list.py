class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("There is nothing inside the list !")
            return
        current_node = self.head # start from head node
        link_list = ''
        while current_node:
            link_list += str(current_node.data) + ' --> ' if current_node.next else str(current_node.data)
            current_node = current_node.next
        print("Link list : ", link_list)

    def get_length(self):
        count = 0
        current_node = self.head
        if current_node:
            count += 1
            current_node = current_node.next
        print("Length of the linked list: ", count)
        return count

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index been given!")

        if index == 0:
            self.insert_at_beginning(data)
            return

        curr_count = 0
        curr_node = self.head
        while curr_node:
            if curr_count == index - 1:
                new_node = Node(data, curr_node.next)
                curr_node.next = new_node
                break
            curr_node = curr_node.next
            curr_count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index been given!")

        if index == 0:
            self.head = self.head.next
            return

        curr_count = 0
        curr_node = self.head
        while curr_node:
            if curr_count == index - 1:
                curr_node.next = curr_node.next.next
                break
            curr_node = curr_node.next
            curr_count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = SinglyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(1, "blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45, 7, 12, 567, 99])
    ll.insert_at_end(67)
    ll.print()
