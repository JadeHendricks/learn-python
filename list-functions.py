lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Jim', 'Oscar', 'Simone']

print(friends)

# append a list on to another list
friends.extend(lucky_numbers)
print(friends)

# add individual elements on to a list
friends.append('Toby')
print(friends)

# add an item into the middle of a list
friends.insert(1, 'Kelly') # insert it at position 1
print(friends)

# remove a single element from a list
friends.remove('Jim')
print(friends)

# remove everything from a list
# friends.clear()
# print(friends)

# remove the last element from a list
friends.pop()
print(friends)

# get the index of a element
print(friends.index('Kevin'))

# check how much time a element shows up in a list
print(friends.count('Jim'))

# sort a list in ascending order
print(friends.sort())
print(lucky_numbers.sort())

# reverse a list
print(lucky_numbers.reverse())

# copy a list
friends2 = friends.copy()
print(friends2)