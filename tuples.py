

# use parentheses instead of square brackets
# loop through the tuple with a for loop:
colors = ('red', 'green', 'blue')
print("The first color is: " + colors[0])

print("\nThe available colors are:")
for color in colors:
    print("- " + color)



# mix raw English strings with tuple values that are stored in variables:
animals = ['dog', 'cat', 'bear']
for animal in animals:
    print("I have a " + animal + ".")



# "%s" and "%d" placeholders. when Python sees this, it looks ahead and pulls in the first argument after the % sign:
# This is called string formatting with a list:
animals = ['dog', 'cat', 'bear']
for animal in animals:
    print("I have a %s." % animal)

# for more than 1 value
animalsanimals  ==  [['dog''dog',,  'cat''cat',,  'bear''bear']]
 printprint(("I have a %s, a %s, and a %s.""I have a %s, a %s, and a %s."  %%  ((animalsanimals[[00],],  animalsanimals[[11],],  animalsanimals[[22]))]))



# string formatting with numbers
number = 23
print("My favorite number is %d." % number)


# strings and numbers
names = ['eric', 'ever']
numbers = [23, 2]
print("%s's favorite number is %d, and %s's favorite number is %d." % (names[0].title(), numbers[0], names[1].title(), numbers[1]))

