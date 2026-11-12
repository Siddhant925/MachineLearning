
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    # Delete a key
    def delete(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print("Key deleted successfully.")
                return

        print("Key not found.")

    # Display hash table
    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Main program
size = int(input("Enter hash table size: "))
h = HashTable(size)

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        h.insert(key, value)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        result = h.search(key)

        if result is not None:
            print("Value:", result)
        else:
            print("Key not found.")

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        h.delete(key)

    elif choice == 4:
        h.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice.")
