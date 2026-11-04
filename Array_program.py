def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    letters = [ch for ch in word if ch.isalpha()]

    array = []
    print("\nAdding the letters:")
    for ch in letters:
        array.append(ch)
    print("Index:", *range(len(array)), sep="  ")
    print("Value:", *array, sep="  ")

    print("\nRemoving the letters:")
    while len(array) != 0:
        print("pop ->", array.pop())
    print("Array is now empty")


if __name__ == "__main__":
    main()
