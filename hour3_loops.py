"""
Hour 3: Loops
Author: Ankith
Description: Sums numbers from 1 to N using a for loop.
"""

N = int(input("Enter a number: "))
total = 0

for i in range(1, N + 1):
    total += i

print(f"The sum from 1 to {N} is {total}.")
