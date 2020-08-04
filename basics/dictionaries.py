tel = {'Jack': 4098, 'Sape': 4139}
print(tel)
tel['Guido'] = 4127
print(tel)
print(tel['Jack'])
del tel['Sape']
print(tel)
print(list(tel))  # puts the keys in a list
tel['Diaz'] = 4129
tel['Leon'] = 3129
print(sorted(tel))

# using the dict constructor to build a dictionary
tel2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# * Looping with for each loop

for k, v in tel.items():
    print("item: " + k, v)
