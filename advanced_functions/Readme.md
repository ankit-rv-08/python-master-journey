# Advanced Functions

## Overview

This module covers advanced Python function concepts essential for production code and technical interviews.

---

## Hour 9: *args, **kwargs, Lambda, Decorators

**Date:** October 27, 2025  
**Duration:** 60 minutes  
**File:** `hour9_args_kwargs_lambda_decorators.py`

### Concepts Covered

#### 1. *args (Variable Positional Arguments)
def sum_all(*numbers):
return sum(numbers)

sum_all(1, 2, 3) # Works
sum_all(1, 2, 3, 4, 5) # Also works - any number of args

text

**Use Case:** When you don't know how many arguments will be passed.

---

#### 2. **kwargs (Variable Keyword Arguments)
def create_profile(**user_info):
for key, value in user_info.items():
print(f"{key}: {value}")

create_profile(name="Ankith", college="NITK", goal="15-20 LPA")

text

**Use Case:** Flexible function signatures, configuration options.

---

#### 3. Lambda Functions
Regular function
def square(x):
return x ** 2

Lambda equivalent
square = lambda x: x ** 2

With map/filter
numbers =​
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

text

**Use Case:** Short, one-off functions with map/filter/sorted.

---

#### 4. Decorators
def timing_decorator(func):
def wrapper(*args, **kwargs):
start = time.time()
result = func(*args, **kwargs)
end = time.time()
print(f"{func.name} took {end - start:.4f}s")
return result
return wrapper

@timing_decorator
def slow_function():
time.sleep(1)
return "Done"

text

**Use Case:** Logging, timing, authentication, caching.

---

### Key Takeaways

1. **\*args** collects positional arguments into a tuple
2. **\*\*kwargs** collects keyword arguments into a dict
3. **Lambda** is for short, one-line functions (use regular functions for complex logic)
4. **Decorators** modify function behavior without changing source code

### Interview Questions You Can Answer

✅ What's the difference between *args and **kwargs?  
✅ When should you use lambda vs regular functions?  
✅ How do decorators work internally?  
✅ Give examples of practical decorator use cases.  
✅ How would you implement memoization?

---

### Next Steps

**Hour 10:** Exception handling and file I/O  
**Hour 11:** Object-Oriented Programming basics
