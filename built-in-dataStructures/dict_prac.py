#countries and their capitals
capitals = {"Nepal": "Kathmandu","italy": "Rome","France": "Paris","Germany": "Berlin","Spain": "Madrid"}
print(capitals)  # Print the dictionary
print(capitals.keys())  # Print the keys of the dictionary
print(capitals.values())  # Print the values of the dictionary
capitals["italy"] = "new "  # Update the value for the key "Italy"
capitals["USA"] = "Washington, D.C."  # Add a new key-value pairS
del capitals ["Nepal"]  # Delete the key "Nepal" and its value
del capitals["Germany"]  # Delete the key "Germany" and its value
sorted_capitals = sorted(capitals)  # Sort the keys of the dictionary
print(sorted_capitals)  # Print the sorted keys
print(capitals)  # Print the updated dictionary
print(capitals["France"])  # Access the value for the key "France" 

for i in capitals:  # Iterate through the keys of the dictionary
    print(i, capitals[i])  # Print each key and its corresponding value