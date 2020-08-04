# A set is and unordered collection with no duplicate items

basket = {"apple", "orange", "pear", "banana", "orange"}
basket2 = set()  # empty set
print(basket)
print(basket2)
print("banana" in basket)  # true
# wecan use matemathical operations such as union, intersection, difference
# and symetric difference with sets
a = set("abracadabra")
b = set('alacazam')
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)  # letters in a and b but not in both
