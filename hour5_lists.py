"""
Hour 5: Lists
Author: Ankith
Description: Finds the largest number in a user-entered list.
"""

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is {largest}.")
