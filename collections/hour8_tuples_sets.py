"""
Hour 8 – Tuples & Sets Fundamentals

- Immutable ordered tuples: creation, use as dict keys.
- Sets: unique collections, membership tests, and set operations.
"""

# Tuple example
point = (10, 20)
print(point[0])

# Set example
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)

fruits.add("date")
fruits.remove("apple")
print(fruits)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference
print(a ^ b)   # Symmetric difference
