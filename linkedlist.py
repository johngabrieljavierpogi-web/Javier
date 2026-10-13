class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Inserted '{data}' at the end.")

    def delete_head(self):
        if not self.head:
            print("Linked list is empty!")
            return
        print(f"Deleted head node with value: {self.head.data}")
        self.head = self.head.next

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None" if elements else "List is empty -> None")



if __name__ == "__main__":
    ll = SinglyLinkedList()

    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)
    
    print("\nCurrent List:")
    ll.display()

    print("\nDeleting head:")
    ll.delete_head()
    
    print("\nUpdated List:")
    ll.display()