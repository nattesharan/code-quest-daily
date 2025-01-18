class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at the end of list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # print all data from list
    def print_list(self):
        if not self.head:
            print("list is empty. Try inserting some data")
            return
        temp = self.head
        result = ''
        while temp:
            result += f'{temp.data}'
            temp = temp.next
            if temp:
                result += '->'
        print(result)
        return result
    
    def insert_after_node(self, key, data):
        if not self.head:
            print("list is empty. Try inserting some data")
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            print("Key not found, reached end of list")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
    
    def delete_by_value(self, value):
        # if value is in first node
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if not current:
            print("Key not found, reached end of list")
            return
        prev.next = current.next
        return
    
    def total_count(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count
    
    def total_count_recur(self, node:Node):
        if not node:
            return 0
        return 1 + self.total_count_recur(node.next)
    
    def delete_by_position(self, pos):
        if pos == 0:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        count = 0
        while current and count != pos:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Key not found, reached end of list")
            return
        prev.next = current.next
        
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    for i in range(4, 14):
        linked_list.insert_at_end(i)
    for i in range(14, 21):
        linked_list.insert_at_beginning(i)
    linked_list.insert_after_node(1, 22)
    linked_list.insert_after_node(13, 23)
    linked_list.print_list()
    linked_list.delete_by_value(20)
    linked_list.delete_by_value(19)
    linked_list.delete_by_value(12)
    linked_list.delete_by_value(40)
    linked_list.delete_by_position(3)
    linked_list.print_list()
    print(linked_list.total_count())
    print(linked_list.total_count_recur(linked_list.head))
    
