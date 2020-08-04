# tuples are a sequence of values separated by commas
# tuples are inmutable and not expandable

t = 123, 456, "hello"  # can have different types of values
print(t)  # tuples are outputed with parenthesis

# empty tuple and tuple with a single element
t2 = ()
t3 = 890,
x, y, z = t  # unpacking tuple values
print(str(x) + " " + str(y) + " " + z)
