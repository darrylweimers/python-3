print("""
----------------------------------------------

TUPLE

- ordered collection of objects
- store and fetch by positional offset (0, 1, 3, ...)
- nested to arbitrary depth
- value cannot be updated (immutable)

----------------------------------------------
\n\n\n""")



print("""
----------------------------------------------

CREATE

Syntax:

    A) tuple_name = (item0 , item1, item2)

    B) tuple_name = item0 , item1, item2

             index    0       1      2

Note:
 - item (any data type including custom class object) separated by comma
 - access by offset start from index 0

Example:
""")
print('tuple_1 = (0, "b", 3.0)')
tuple_1 = (0, "b", 3.0)
print("tuple 1:", tuple_1)

print('tuple_2 = 0.5, "abc"')
tuple_2 = 0.5, "abc"
print("tuple 2:", tuple_2)

print("""
----------------------------------------------

SIZE

Syntax:

   size = len(tuple)

Example:
""")
print("tuple:", tuple_1)

print("Number of item in tuple:", len(tuple_1))



print("""
----------------------------------------------

FETCH ITEM

Syntax:

    item = tuple[index]

Example:
""")
print("tuple:", tuple_1)

print("First item:", tuple_1[0])
print("Last item:", tuple_1[len(tuple_1) - 1])



print("""
----------------------------------------------

MERGE

Syntax:

    new_tuple = tuple_1 + tuple_2

Example:
""")
print("tuple 1:", tuple_1)
print("tuple 2:", tuple_2)
resultant_tuple = tuple_1 + tuple_2
print("resultant tuple:", resultant_tuple)

