# kwyword in
message = "I like cats and dogs."
dog_present = 'dog' in message
print(dog_present)


# find method
message = "I like cats and dogs."
dog_index = message.find('dog')
print(dog_index)

# find the last instance of a substring
message = "I like cats and dogs, but I'd much rather own a dog."
last_dog_index = message.rfind('dog')
print(last_dog_index)

# repalce a substring
message = "I like cats and dogs, but I'd much rather own a dog."
message = message.replace('dog', 'snake')
print(message)


# counting occurances of a asubstring
message = "I like cats and dogs, but I'd much rather own a dog."
number_dogs = message.count('dog')
print(number_dogs)


# split string
message = "I like cats and dogs, but I'd much rather own a dog."
words = message.split(' ')
print(words)