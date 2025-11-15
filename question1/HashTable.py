class HashTable:
    class Node:
        def __init__(self, key, value):
            """
            Represents a node with key, value, and pointer
            to implement hash table with linked-list
            """
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=10):
        """
        Represents an empty hash table with a specified capacity

        This hash table uses linked-list implementation
        for efficient operations such as insert, search,
        edit, and delete
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity   # array of linked lists (chains)

    def _hash(self, key):
        """
        Handles hashing of key using the hash() function
        to return index.

        Note: capacity represents hash table size
              formula is applied below
        """
        return hash(key) % self.capacity

    def insert(self, key, value):
        """
        Insert the key-value pair into the hash table

        Each bucket is implemented using linked-lists
        uses separate chaining to handle collisions
        """
        index = self._hash(key)
        head = self.table[index]

        # Case 1: If no chain at this index, then create new node
        if head is None:
            self.table[index] = self.Node(key, value)
            self.size += 1
            return

        # Dase 2: if key exists, update it
        current = head
        while current:
            # If the same key is found, then update its value
            if current.key == key:
                current.value = value
                return

            # Move to the next item in the chain
            current = current.next

        # Case 3: Insert new node at head
        new_node = self.Node(key, value)
        new_node.next = head
        self.table[index] = new_node
        self.size += 1

    def search(self, key):
        index = self._hash(key)

        # Current will point to the first item in the chain
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value

            # If key is not yet found, move to the next item
            current = current.next

        # If the key is not found, then return None
        return None

    def edit(self, key, new_value):
        index = self._hash(key)
        current = self.table[index]

        while current:
            # If the key value is found, then update its value
            if current.key == key:
                current.value = new_value
                return True
            current = current.next

        return False  # Not found

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                # Deleting head of chain
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                self.size -= 1
                return True

            prev = current
            current = current.next

        return False  # Not found

    def __len__(self):
        return self.size

    def print_table(self):
        print("")
        for i in range(self.capacity):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current:
                print(f"[{current.key}={current.value}] -> ", end="")
                current = current.next
            print("")