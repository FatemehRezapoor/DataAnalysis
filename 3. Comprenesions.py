# July 2020
# COMPREHENSION / ONE LINE CODE

# 1. PRINT A FOR LOOP [list]
myloop=[]
for i in range(10):
    myloop.append(i**2)
print(myloop)
# Comprehension:
myloop=[i**2 for i in range(10)]
print(myloop)

# 2. PRINT THE COMPREHENSION (TIPS) [list]
# When you use a comprehension, you create an object. When you use print to print out, you will get the object presentation.
print((n**2 for n in  range(3)))
# To get a different presentation you can:
# * Print the results in a list
print([n**2 for n in  range(3)])
# ** Print the results seperately
print(*(n**2 for n in  range(3)))

# 3. COMPREHENSION : FOR + IF [list]
myloop=[i**2 for i in range(10) if i%3==0]
print(myloop)

# 4. COMPREHENSION: DICTIONARY
mydic={i:i**2 for i in range(10) if i%3==0}
print(mydic)

#5. READ DICTIONARY/CREATE SET AND DICTIONARY
capitals = {'United States': 'Washington, DC','France': 'Paris','Italy': 'Rome'}
for i in capitals:
    print(capitals[i])

mycap={capitals[key] for key in capitals}
print(type(mycap))

mycapdic={capitals[key]:key for key in capitals}
print(mycapdic)

#6. GENERATOR EXPRESSION
print(sum(i for i in range(10)))
print(sum([i for i in range(10)])) # Creates a list and saves in the memory