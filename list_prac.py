list_a = [2,3,4,5,6,7,8,9,10] # Create a list with initial values

print(list_a[3]) # Accessing the 4th element (index 3)
print(list_a) # Access the element at index 3
list_a[3] = 100     # Change the value at index 3
list_a.insert(list_a[6], 200) # Insert an element at the end
list_a.append(300) # Add an element at the end
list_a.extend([400, 500, 600]) # Add multiple elements at once
list_a.pop(0)  # Remove the first element
list_a.remove(100) # Remove the element with value 100
del list_a[4] # Delete the element at index 4
list_a.remove(300) # Remove the element with value 300
list_a.sort() # Sort the list in ascending order
list_a.reverse() # Reverse the order of the list
print(list_a) # Print the modified list
for item in list_a: # Iterate through the list
    print(item) # Print each item  

#python list comprehension
numbers = [number*number for number in range(1, 11)] # Create a list of squares of numbers from 1 to 10
print(numbers) # Print the list of squares
numbers = [numbers*X for X in range(1,6)]
print(numbers) # Print the list of multiples of X from 1 to 5
