animals = ("lion", "monkey", "cheetah", "gorilla", "chimpanzee", "rhino", "elephant", "panda", "cheetah", "lemur")

(a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9) = animals

print(animals.index("gorilla"))

animal_to_find = "chimpanzee"

if animal_to_find in animals:
    print(f'{animal_to_find} was found')

print(a_0)

animal_list = list(animals)

animal_list.extend(["zebra", "ostrich", "peacock"])

new_animals = tuple(animal_list)

print(new_animals)