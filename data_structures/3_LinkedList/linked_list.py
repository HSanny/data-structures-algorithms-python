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
        while current_node:
            count += 1
            current_node = current_node.next
        # print("Length of the linked list: ", count)
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

    def insert_after_value(self, data_after, data_to_insert):
        # search for first occurrence of data_after
        # insert data_to_insert after data_after
        if self.head is None:
            raise Exception("The list is empty!")
        current_node = self.head
        while current_node:
            if str(current_node.data) == str(data_after):
                new_node = Node(data_to_insert, current_node.next)
                current_node.next = new_node
            current_node = current_node.next

    def remove_by_value(self, data):
        # remove first node that contains data
        if self.head is None:
            raise Exception("The list is empty!")

        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        print("value given is not in the linked list")

if __name__ == '__main__':
    # ll = SinglyLinkedList()
    # ll.insert_values(["banana", "mango", "grapes", "orange"])
    # ll.print()
    # ll.insert_at(1, "blueberry")
    # ll.print()
    # ll.remove_at(2)
    # ll.print()
    #
    # ll.insert_values([45, 7, 12, 567, 99])
    # ll.print()
    # ll.insert_at_end(67)
    # ll.print()

    ll = SinglyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()