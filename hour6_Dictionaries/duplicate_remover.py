"""
Hour 1 – Duplicate Remover

Removes duplicates from a list using dictionary keys to preserve order.
"""

lst = ["ghost", "cod", "ghost", "ghost", "frosty"]
unique = {}
result = []
for x in lst:
    if x not in unique:
        unique[x] = True
        result.append(x)
print(result)
# Output: ['ghost', 'cod', 'frosty']
