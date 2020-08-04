words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w)


# iterating over a sequence of numbers
for i in range(5):
    print(i)
print("\n")

for i in range(0, 10, 3):  # the third number specifies the increment
    print(i)

for i in reversed(range(1, 10, 2)):  # loop in reverse
    print(i)

# the range is an iterable which can be used with functions
sum(range(4))  # 6
list(range(6))  # list from 0 to 5

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# Looping through two lists at the same time
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# sorting and putting the elements in a set
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
