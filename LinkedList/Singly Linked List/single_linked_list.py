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
