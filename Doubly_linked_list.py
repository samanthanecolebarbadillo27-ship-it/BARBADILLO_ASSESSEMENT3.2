class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        parts, current = [], self.head
        while current:
            parts.append(current.data)
            current = current.next
        print("None <-> " + " <-> ".join(parts) + " <-> None")

    def remove_from_tail(self):
        while self.tail is not None:
            print("Remove", self.tail.data)
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
        print("List is now empty")


def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    dll = DoublyLinkedList()

    print("\nAdding the letters:")
    for ch in word:
        if ch.isalpha():
            dll.add(ch)
    dll.display()

    print("\nRemoving the letters starting from the tail:")
    dll.remove_from_tail()


if __name__ == "__main__":
    main()