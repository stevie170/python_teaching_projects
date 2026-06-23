grocery_list = ['apples', 'bananas', 'chips']

# Append: Add a new item to the end of the list
grocery_list.append('milk')
print(grocery_list) # Output: ['apples', 'bananas', 'chips', 'milk']

# Insert: Add one item to a specific index
# We'll insert chocolate in the front of the list since it's the most important thing to purchase
grocery_list.insert(0, 'chocolate')
print(grocery_list) # Output: ['chocolate', 'apples', 'bananas', 'chips', 'milk']

# Extend: Add sequence items one by one to a sequence
# We'll extend the list with another list of items
grocery_list.extend(['bread', 'eggs'])
print(grocery_list) # Output: ['chocolate', 'apples', 'bananas', 'chips', 'milk', 'bread', 'eggs']

# Remove: Remove specified item by its value
grocery_list.remove('chips')
print(grocery_list) # Output: ['chocolate', 'apples', 'bananas', 'milk', 'bread', 'eggs']

# Pop: Remove and return the last item of a list
last_item = grocery_list.pop()
print(grocery_list) # Output: ['chocolate', 'apples', 'bananas', 'milk', 'bread']
print('Popped item was ', last_item) # Output: Popped item was eggs

# We can also remove a specific item by index using pop()
# We'll remove 'bananas' from the list
removed_item = grocery_list.pop(2)
print(grocery_list) # Output: ['chocolate', 'apples', 'milk', 'bread']
print('Popped item was ', removed_item) # Output: Popped item was bananas
