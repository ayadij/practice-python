# Start with a list containing several names.
names = ['guido', 'tim', 'jesse']

# Ask the user for a name.
new_name = raw_input("Please tell me someone I should know: ")

# Add the new name to our list.
names.append(new_name)

# Show that the name has been added to the list.
print(names)