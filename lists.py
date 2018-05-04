

cars = ['bmw', 'toyota', 'audi']

for car in cars:
    print("Wow, nice " + car.title() + "!")



# notice the use of plural and singular

colors = ['brown', 'orange', 'yellow']

color = colors[0]
print(color.title())



# accessing the second to last item in the list

peppers = ['banana pepper', 'green pepper', 'lemon pepper']

pepper = peppers[-2]
print(pepper.title())



# notice the use of indentation

dogs = ['ridgeback', 'labrador', 'wiener']

for dog in dogs:
    print('I like ' + dog + 's.')
    print('No, I really really like ' + dog +'s!\n')
    
print("\nThat's just how I feel about dogs.")



# index starts at 0 so remember to add 1 when enumerating lists

fruits = ['strawberry', 'orange', 'grapes']

print("Results for the dog show are as follows:\n")
for index, fruit in enumerate(fruits):
    place = str(index + 1)
    print("Place: " + place + " Fruit: " + fruit.title())



# len() to fing length of a list

usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print(user_count)



# slicing the list

usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Grab the first three users in the list.
first_batch = usernames[0:3]

for user in first_batch:
    print(user.title())



# a list from a string
message = "Hello!"

for letter in message:
    print(letter)



# split with each character being an element 
message = "Hello world!"

message_list = list(message)
print(message_list)