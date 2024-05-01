"""
Write a method that add or updates a key with a value
You have to complete the put() method of a HashTable class that is already given to you. The put method should accept two parameters: a key value and a data value. The data value is found through the key value.
The method returns nothing.

The method should return MemoryError if the HastTable is full. The method will try to find the key, if it's found,
it will update its value. If it is not found, it will add the key and data values to the HashTable as a HashItem,
being careful with not overwriting any other HashItem. It would also update the used_slots counter.
"""


class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'


class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        # return len(key) % self.size
        return sum((index + 1) * ord(char) * ord(char) for index, char in enumerate(key)) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.

        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        # Start to search from the given position
        current = start

        # While that position is in use, enter the loop
        while self.slots[current]:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size

            # If we reach again the given position, it means
            # a whole cycle has been completed and there was no free positions available
            if current == start:
                return None

        # After the loop, current points to a free position
        return current

    def _find_key(self, start, key):
        """
        Starting from 'start' try to find 'key'.

        Parameters:
        - 'start': Starting index
        - 'key': The key to be found

        Returns: The index position of the key or None if not found
        """
        # Start to search from the given position
        current = start

        # While current position is occupied, and it's not the key, enter the loop
        while self.slots[current] and self.slots[current].key != key:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            # If we reach again the given position, that means
            # a whole cycle has been completed and the key was not found
            if current == start:
                return None

        # After the loop, current points to a free position or
        # to the position with the key
        if self.slots[current]:
            return current
        else:
            return None

    def put(self, key, value):
        """
        Add or updates a key with a value in the hash table

        Parameters:
        - 'key': The key to add or update.
        - 'value': The value of the key

        Returns: None
        """
        # Calculate the hash value of the given key
        hash_value = self._hash(key)

        # Find if the key already exists
        index = self._find_key(hash_value, key)

        # If the key exists, update its value
        if index is not None:
            self.slots[index].value = value
        else:
            # Find a free slot
            free_slot = self._find_free_slot(hash_value)
            # If a free slot is found, add a new HashItem
            if free_slot is not None:
                self.slots[free_slot] = HashItem(key, value)
                self.used_slots += 1
            else:
                # If no free slot is found, raise a MemoryError
                raise MemoryError("HashTable is full")


h = HashTable()
h.put("Name", "HashTable")
print(h.slots[229])  # {Name: HashTable}

ht = HashTable()

try:
    for i in range(57):
        ht.put(f"key{i}", i)
except MemoryError:
    pass

print(ht.slots)  # [None, None, {key26: 26}, None, None, None, None, None, None, None, None, {key43: 43},
# None, None, {key2: 2}, {key20: 20}, {key44: 44}, None, {key42: 42}, None, None, None, None, {key39: 39},
# None, None, None, {key45: 45}, None, None, None, None, None, None, None, {key27: 27}, {key41: 41}, None,
# None, None, None, None, None, None, None, None, None, None, None, None, {key46: 46}, None, None, None,
# None, None, None, None, None, None, None, None, {key4: 4}, {key40: 40}, None, None, {key7: 7}, None, None,
# None, None, None, None, None, None, None, None, None, {key28: 28}, {key13: 13}, None, None, {key14: 14},
# {key47: 47}, None, None, {key12: 12}, None, None, None, None, None, None, None, None, {key15: 15}, None,
# None, None, None, None, None, None, {key11: 11}, None, None, None, None, None, None, None, {key33: 33},
# None, None, {key34: 34}, None, None, None, {key16: 16}, {key32: 32}, None, None, None, None, None, None,
# {key48: 48}, {key35: 35}, None, None, {key1: 1}, {key10: 10}, {key29: 29}, None, None, {key31: 31}, None,
# None, None, None, None, None, {key6: 6}, None, None, None, None, None, None, None, {key36: 36}, {key17: 17},
# None, None, None, None, None, None, None, None, None, None, {key3: 3}, {key30: 30}, None, None, None, None,
# None, None, None, None, None, None, None, {key53: 53}, None, None, {key54: 54}, {key49: 49}, None, None,
# {key52: 52}, {key37: 37}, None, None, None, None, None, None, None, {key55: 55}, None, None, {key9: 9},
# {key18: 18}, None, None, None, {key51: 51}, None, None, None, None, None, None, None, None, None, None, None,
# None, None, None, {key56: 56}, None, None, None, None, {key23: 23}, None, None, {key24: 24}, None, None, None,
# {key5: 5}, {key22: 22}, {key38: 38}, {key50: 50}, None, None, None, None, None, {key25: 25}, None, None, None,
# None, None, None, None, {key21: 21}, None, None, None, {key19: 19}, None, None, None, None, None, None, {key0: 0},
# {key8: 8}]
