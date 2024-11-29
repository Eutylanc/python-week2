# Task 1: Create a list of integers and compute their sum
print("Task 1: Sum of a list of integers")
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print(f"The sum of the integers is: {sum(numbers)}")


# Task 2: Tuple of favorite books and print each book on a new line
print("\nTask 2: Favorite books")
favorite_books = ("1984", "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice", "Moby Dick")
print("My favorite books are:")
for book in favorite_books:
    print(book)

# Task 3: Dictionary to store information about a person
print("\nTask 3: Information about a person")
person = {}
person['name'] = input("Enter your name: ")
person['age'] = int(input("Enter your age: "))
person['favorite_color'] = input("Enter your favorite color: ")
print("Here is the information you provided:")
print(person)


# Task 4: Find common elements in two sets
print("\nTask 4: Common elements in two sets")
set1 = set(map(int, input("Enter the first set of integers separated by spaces: ").split()))
set2 = set(map(int, input("Enter the second set of integers separated by spaces: ").split()))
common_elements = set1 & set2
print(f"The common elements are: {common_elements}")

# Task 5: Words with an odd number of characters
print("\nTask 5: Words with odd number of characters")
words = input("Enter a list of words separated by spaces: ").split()
odd_length_words = [word for word in words if len(word) % 2 != 0]
print(f"Words with an odd number of characters: {odd_length_words}")
