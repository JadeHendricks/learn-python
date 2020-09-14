print("Giraffe\nAcademy")

phrase = "Giraffe Academy"

# concatenation
print(phrase + " is cool")

# using funtions on strings
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())

# using funtions in conjunction
print(phrase.upper().isupper)

# getting the length of a string
print(len(phrase))

# get individual characters inside a string
print(phrase[0])
print(phrase[3])

# get an index of where a specific character is
print(phrase.index('G'))
print(phrase.index('Acad'))

# using replace to replace a word
print(phrase.replace('Giraffe', 'Elephant'))