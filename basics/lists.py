# lists are mutable and expandable
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[-2:])  # returns last two elements

print(squares + [36, 49, 64])  # concatenating
print("len of squares: " + str(len(squares)))

# * adding and removing elements
squares.append(36)

squares2 = [49, 64, 81, 100]
squares.extend(squares2)  # appends the list
print(squares)

# removes the first value which is equal to the parameter given
squares.remove(1)
squares.pop()  # removes and returns the last value, an index can be specified

# * List comprehension
# the brackets contain an expression followed by a for loop
squares3 = [x**2 for x in range(10)]

# adds the combination of the numbers that dont match
comp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(comp)
del comp[0]  # removes the index of a list
