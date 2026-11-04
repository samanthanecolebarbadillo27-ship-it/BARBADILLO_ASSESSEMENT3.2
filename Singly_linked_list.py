class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        parts, current = [], self.head
        while current:
            parts.append(current.data)
            current = current.next
        print(" -> ".join(parts) + " -> None")

    def remove_all(self):
        while self.head is not None:
            print("Remove", self.head.data)
            self.head = self.head.next
        print("List is now empty")


def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    lst = SinglyLinkedList()

    print("\nAdding the letters:")
    for ch in word:
        if ch.isalpha():
            lst.add(ch)
    lst.display()

    print("\nRemoving the letters:")
    lst.remove_all()


if __name__ == "__main__":
    main()