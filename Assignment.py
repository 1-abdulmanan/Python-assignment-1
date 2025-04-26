# Question 1

my_list = [1, 2, 3, 4, 5, 1.1, 2.2, 3.3, 4.4, 5.5, "one", "two", "three", "four", "five"]
print(my_list)

# Question 2

my_list.append(100)
print(my_list)

# Question 3

empty_list = []
empty_list.insert(0, "first element")
empty_list.insert(1, "second element")
empty_list.insert(1, "inserted at index 1")
print(empty_list)

# Question 4

for item in my_list:
    print(item)

# Question 5

int_list = [10, 3, 5, 7, 2, 8, 1, 9, 4, 6]
# Ascending order
int_list.sort()
print("Ascending:", int_list)
# Descending order
int_list.sort(reverse=True)
print("Descending:", int_list)

# Question 6

str_list = ["banana", "apple", "cherry", "date", "fig", "grape", "elderberry", "honeydew", "kiwi", "lemon"]
# Ascending order
str_list.sort()
print("Ascending:", str_list)
# Descending order
str_list.sort(reverse=True)
print("Descending:", str_list)

# Question 7

user_list = []
while True:
    element = input("Enter the element to insert: ")
    position = int(input("Enter the position to insert at: "))    
    if position <= len(user_list):
        user_list.insert(position, element)
    else:
        print(f"Invalid position! List length is {len(user_list)}.")
    cont = input("Do you want to continue? (yes/no): ").lower()
    if cont != 'yes':
        break
print(user_list)

# Question 8

nums = [10, 20, 5, 30, 15]
print("Minimum:", min(nums))
print("Maximum:", max(nums))

# Question 9

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
print(list1)
# Output will be [1, 2, 3, [4, 5, 6]]

# Question 10

mylist = []
while True:
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Remove")
    print("4. Pop")
    print("5. Copy")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        elem = input("Enter element to append: ")
        mylist.append(elem)
        print("List after append:", mylist)
    elif choice == '2':
        pos = int(input("Enter position: "))
        elem = input("Enter element to insert: ")
        if pos <= len(mylist):
            mylist.insert(pos, elem)
            print("List after insert:", mylist)
        else:
            print("Invalid position!")
    elif choice == '3':
        elem = input("Enter element to remove: ")
        if elem in mylist:
            mylist.remove(elem)
            print("List after remove:", mylist)
        else:
            print("Element not found!")
    elif choice == '4':
        if mylist:
            popped = mylist.pop()
            print(f"Popped element: {popped}")
            print("List after pop:", mylist)
        else:
            print("List is empty!")
    elif choice == '5':
        copied_list = mylist.copy()
        print("Copied List:", copied_list)
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
