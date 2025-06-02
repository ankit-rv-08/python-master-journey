def sum_to_n(n):
    """Return sum of numbers from 1 to n."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

N = int(input("Enter a number: "))
result = sum_to_n(N)
print(f"The sum from 1 to {N} is {result}")
