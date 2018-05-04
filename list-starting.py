# Create an empty list to hold our users.
usernames = []

# Add some users.
usernames.append('bernice')
usernames.append('cody')
usernames.append('aaron')

# Greet all of our users.
for username in usernames:
    print("Welcome, " + username.title() + '!')