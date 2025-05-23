import pickle

class Foo:
    attr = 'A class attribute'

foo:Foo = Foo()
picklestring: bytes = pickle.dumps(foo)
print(type(picklestring))

foo:Foo = pickle.load(picklestring)
if isinstance(foo,Foo):
    print("Yes")
else:
    print("No")

