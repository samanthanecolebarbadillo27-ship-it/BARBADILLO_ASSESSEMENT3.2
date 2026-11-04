from collections import deque


def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    queue = deque()

    print("\nAdding the letters (front is the first letter added):")
    for ch in word:
        if ch.isalpha():
            queue.append(ch)
            print(f"append({ch}) -> {' '.join(queue)}")

    print("\nRemoving the letters:")
    while len(queue) != 0:
        print("popleft ->", queue.popleft())
    print("Queue is now empty")


if __name__ == "__main__":
    main()