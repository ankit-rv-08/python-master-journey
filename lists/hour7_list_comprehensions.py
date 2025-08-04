"""
Hour 7 – List Comprehensions & Built-Ins

Master concise list creation, filtering, map/filter, enumerate, and basic built-ins.
"""

nums = list(range(1, 21))

# Squares of even numbers
evens_squared = [x**2 for x in nums if x % 2 == 0]
print("Squares of evens:", evens_squared)

# Filter negative numbers
nums_with_neg = [4, -1, 9, -3, 5]
positives = list(filter(lambda x: x >= 0, nums_with_neg))
print("Filtered positives:", positives)

# Enumerate example
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# Sorting, summing, length
to_sort = [4, 2, 9, 1]
print("Sorted:", sorted(to_sort))
print("Sum:", sum(to_sort))
print("Length:", len(to_sort))
