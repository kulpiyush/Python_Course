"""_summary_
"""
x = None
print(x)
x = 5
print(x)

# Numeric types (int, float, complex)
a = 5
b = 5.05
c = 5 + 5j
print(type(a))
print(type(b))
print(type(c))

a = 10
b = 20
if (a > b):
    print("Hello")
else:
    print("ok")

# Sequence types (string, list, tuple, Range)
# String
my_name = "Piyush"
print(my_name)

# List
my_list = ["Piyush", 5, 5.4]
print(my_list)
# Indexing
print(my_list[2])

# Tuple
my_tuple = ("Piyush", 5, 5.4)
print(my_tuple)
# Indexing
print(my_tuple[0])

# Range
my_range = range(1, 10, 2)
q = list(my_range)
print(q)
r = list(range(1, 10))
print(r)

# Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)
s = {50, 77, 60, 14, 15}
print(s)

lst = [10, 5, 6]
a = set(lst)
print(a)

# Dictionary
d = {10: "unwired", 20: "wireless"}
print(d)
print(d[10])

di = {"name": "Piyush", "age": 25}
print(di["name"])