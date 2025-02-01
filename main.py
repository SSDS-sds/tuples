#Creating a tuple
pets = ("dog","cat","parrot")
print(pets)

#Accessing values from a tuple
fave_pet = pets[1]
print(f"My {fave_pet} is Mufasa")

#Packing tuples
fave_subject = ("My","favourite","subject","is","computer","science.")
for word in fave_subject:
    print(word,end = " ")

#Unpacking in tuples
cities = ("london","paris","brussels")
english,french,belgian = cities
print()
print(f"{english} is an english city.")
print(f"{french} is a french city.")
print(f"{belgian} is a belgian city")

#Tuples without brackets
names = "Jack","John","Joshua"
print(names)

#Nested tuples
animals = ("Jackel", "Sheep", "Chick",("Rex","Bab","Chen"))
lamb = animals[1]
lamb_name = animals[3][1]
print(f"{lamb_name} {lamb_name} black {lamb}")