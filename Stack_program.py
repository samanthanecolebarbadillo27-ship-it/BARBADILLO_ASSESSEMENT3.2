def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    stack = []

    print("\nAdding the letters (top is the last letter added):")
    for ch in word:
        if ch.isalpha():
            stack.append(ch)
            print(f"Append ({ch}) -> {' '.join(stack)}")

    print("\nRemoving the letters:")
    while len(stack) != 0:
        print("pop ->", stack.pop())
    print("Stack is now empty")


if __name__ == "__main__":
    main()