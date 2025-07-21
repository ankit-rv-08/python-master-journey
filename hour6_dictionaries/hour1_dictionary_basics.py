"""
Hour 1 – Python Dictionaries: Basic CRUD Operations

Summary:
- Creating, reading, updating, and deleting dictionary entries
- Key dictionary methods practiced
"""

# Create dictionary
student_ages = {"Ankith": 21, "Ghost": 23}

# Read value
print("Ankith age:", student_ages["Ankith"])

# Add/Update value
student_ages["Price"] = 22
print("Updated dict:", student_ages)

# Delete key
del student_ages["Ghost"]
print("After delete:", student_ages)
