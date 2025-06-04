# 1. Accept user input to create a list of integers and compute the sum
numbers = input("Enter a list of integers with spaces").split()
int_list = [int(num) for num in numbers]
total_sum = sum(int_list )
print(f"The sum of the integers is: {total_sum}")


print("\n" + "-"*40 + "\n")

# 2. Create a tuple of favorite books and print each on a separate line
favorite_books = ("To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby")
for book in favorite_books:
    print(book)

    
print("\n" + "-"*40 + "\n")

# 3 Use a dictionary to store person info from user input
person = {}
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["city"] = input("Enter your city: ")
print(f"Person Information: {person}" )

print("\n" + "-"*40 + "\n")

