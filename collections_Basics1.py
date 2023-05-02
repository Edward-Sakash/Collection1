
"""car_brands = ['BMW', 'Audi', 'Volkswagen']

for brand in car_brands:
    print(brand)

car_brands.append('Volvo')

print(car_brands)

car_brands.pop(0)

print(car_brands)"""

print("--------------------------------")

# Task 1

fruits = []
fruits.append('Apples')
fruits.append('Cherries')
fruits.append('Strawberries')

for fruit in fruits:
    print(fruit)

print("--------------------------------")

# Task 2

cities = ['London', 'Paris', 'Berlin', 'Amsterdam']
print("The capital city of Germany is: " + cities[2])


print("--------------------------------")

# Task 3
#solution 1
colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']

# remove 'green' and 'white' from the list
colors.remove('green')
colors.remove('white')

# print the remaining colors
for color in colors:
    print(color)

print("--------------------------------")

#solution 2
colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']

# remove 'green' and 'white' from the list
colors.pop(2)
colors.pop(4)

# print the remaining colors
for color in colors:
    print(color)

print("--------------------------------")

# Task 4
# solution 1
letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']

# combine the letters into a string 'penguin'
word_expected = ''.join(letters)

# capitalize the string 'penguin'
word_expected = word_expected.capitalize()

# print the string 'penguin'
print(word_expected)

print("--------------------------------")

# solution 2

letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']

# combine the letters into a string 'penguin' using the append method
final_word = ""
for letter in letters:
    final_word += letter

# capitalize the string 'penguin'
final_word = final_word.capitalize()

# print the string 'penguin'
print(final_word)


