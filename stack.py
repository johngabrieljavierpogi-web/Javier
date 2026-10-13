class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed '{item}' to stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None
        popped_item = self.items.pop()
        print(f"Popped '{popped_item}' from stack.")
        return popped_item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack (Top to Bottom):", list(reversed(self.items)))

# Example usage:
if __name__ == "__main__":
    s = Stack()
    s.push("Data 1")
    s.push("Data 2")
    s.display()
    s.pop()
    s.display()