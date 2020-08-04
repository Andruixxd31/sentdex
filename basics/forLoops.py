words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w)


# iterating over a sequence of numbers
for i in range(5):
    print(i)
print("\n")

for i in range(0, 10, 3):  # the third number specifies the increment
    print(i)

# the range is an iterable which can be used with functions
sum(range(4))  # 6
list(range(6))  # list from 0 to 5
