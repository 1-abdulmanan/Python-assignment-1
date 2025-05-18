# Q1: Create a dictionary with 5 elements
my_dict = {
    "name": "Alice",
    "age": 2500,
    "city": "grave",
    "email": "alice@example.com",
    "gender": "Female"
}
print("Q1 - Dictionary with 5 elements:", my_dict)

# Q2: Perform append operation (Note: dictionaries use key assignment to add items)
my_dict["country"] = "USA"  # Adding a new key-value pair
print("Q2 - After appending one item:", my_dict)

# Q3: Create an empty dictionary and add items using assignment (insert is not used with dictionaries)
empty_dict = {}
empty_dict["id"] = 101
empty_dict["name"] = "John"
empty_dict["salary"] = 50000
print("Q3 - Dictionary after inserting items:", empty_dict)

# Q4: Use a for loop to access keys using the keys() function
print("Q4 - Keys in the dictionary:")
for key in my_dict.keys():
    print("Key:", key)

# Q5: Create a dictionary with 10 elements and print values using values() function
dict_10 = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
    "f": 6, "g": 7, "h": 8, "i": 9, "j": 10
}
print("Q5 - Values in the dictionary:")
print(dict_10.values())

# Q6: Delete item using popitem() function
removed_item = dict_10.popitem()  # Removes the last inserted item
print("Q6 - Removed item using popitem():", removed_item)
print("Q6 - Dictionary after popitem():", dict_10)

# Q7: Create a dictionary and add list as values
student_courses = {
    "Alice": ["Math", "Science", "English"],
    "Mr. Bean": ["History", "Math"],
    "Charlie-Chaplin": ["Biology", "Chemistry"]
}
print("Q7 - Dictionary with lists as values:", student_courses)
