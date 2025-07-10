my_list = [1, 2, 3]

# --- List Operations ---
print("List Operations")
print("Original list:", my_list)

#Appending
my_list.append(4)
print("After append:", my_list)

#Insterting values
my_list.insert(1, 5)
print("After insert at index 1:", my_list)

# Popping
my_list.pop()
print("After pop:", my_list)

# Changing a value
my_list[0] = 10
print("After modifying first element:", my_list)

# Iterating
for item in my_list:
    print("List item:", item)


# Wierd Stuff
list1 = ["hola"]
list2= ["amigo"]
print("list1: " , list1)
print("list2: " , list2)

list3 = list1+list2

list4= list1.append(list2)

list5= list1.insert(1,list2)

list6 = ["1","2","3","4"]
list6[1] = list2

print("list3: " , list3)
print("list4: " , list4)
print("list5: " , list5)

print("list1: " , list2)
print("list2: " , list2)

print("list6: " , list6)


my_tuple = (1, 2, 3)

# --- Tuple Operations ---
print("\nTuple Operations")
print("Original tuple:", my_tuple)

# Appending
# nuh uh

# Insterting values
# nuh uh

# Popping
# nuh uh

# Changing a value
# nuh uh

# Iterating
for item in my_tuple:
    print("Tuple item:", item)


my_set = {1, 2, 3}

# --- Set Operations ---
print("\nSet Operations")
print("Original set:", my_set)

# Adding to set
my_set.add(4)
print("After add:", my_set)

# Removing from set
my_set.remove(2)
print("After remove:", my_set)

# Iterating through set
for item in my_set:
    print("Set item:", item)



my_dict = {'a': 1, 'b': 2, 'c': 3}

# --- Dictionary Operations ---
print("\nDictionary Operations")
print("Original dictionary:", my_dict)

# Adding to dictionary
my_dict['d'] = 4
print("After adding new key-value pair:", my_dict)

# Modifying value
my_dict['a'] = 10
print("After modifying value of key 'a':", my_dict)

# Popping from dictionary
my_dict.pop('b')
print("After pop key 'b':", my_dict)

# Iterating through dictionary
for key, value in my_dict.items():
    print(f"Dictionary item: {key} -> {value}")
