def f(arg=5):  # giving a default value to the functions
    print(arg)


f(7)
f()  # since no value was given arg will be 5

# with a mutable objectthe deafault value can be accumulated to stop this use None


def func(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


def say(andres, jose="Hello"):
    print("andres says: " + andres)
    print("jose says: " + jose)


say("Hey", "Hi")
say("Hey")
say(jose="Bye", andres="see ya")  # giving keyword arguments
