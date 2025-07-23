"""
Hour 2 – Dictionary Looping & Modification
- Looping through keys, values, items
- Updating and removing entries
"""

person = {'name': 'Max', 'age': 28, 'city': 'New York'}
print("Keys:")
for k in person:
    print(k)
print("\nValues:")
for v in person.values():
    print(v)
print("\nKey-Value pairs:")
for k, v in person.items():
    print(f"{k}: {v}")

person['profession'] = "Dev"
person.update({'age': 30, 'city': 'Boston'})
del person['city']
removed = person.pop('profession', None)
print("\nAfter updates and removals:", person)
