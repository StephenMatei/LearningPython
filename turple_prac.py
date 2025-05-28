var1 = ("hello") # This is a string, not a tuple
print(type(var1))

var2 = ("hello",) # This is a tuple with one element
print(type(var2))  # This will show <class 'tuple'>

var3 ="hello",  # This is a tuple with one element, but the comma is necessary
print(type(var3))  # This will also show <class 'tuple'>

#accessing tuple elements unsing indexing
letters = ("a", "b", "c", "d", "e")
print(letters[0])  # Accessing the first element
print(letters[1])  # Accessing the second element
print(letters[2])  # Accessing the third element

#negative indexing
print(letters[-1])  # Accessing the last element    
print(letters[-2])  # Accessing the second last element

#slicing tuples
print(letters[1:4])  # Slicing from index 1 to 3 (not including 4)
print(letters[:3])   # Slicing from the start to index 2
print(letters[2:])   # Slicing from index 2 to the end
print(letters[-3:])  # Slicing from the third last element to the end

# Tuple unpacking
a, b, c, d, e = letters  # Unpacking the tuple into variables
print(a)  # Output: a
print(b)  # Output: b

#turple methods
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(2))  # Count occurrences of 2 in the tuple
print(my_tuple.index(3))  # Find the index of the first occurrence of 3 in the tuple