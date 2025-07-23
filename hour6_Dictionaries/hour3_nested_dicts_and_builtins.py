"""
Hour 3 – Nested Dictionaries & Built-in Methods

- Define and navigate nested dictionaries
- Apply built-in and analytics functions on dict data
"""

students = {
    "ankith": {"age": 21, "major": "CSE", "cgpa": 9.2},
    "ghost": {"age": 23, "major": "AI", "cgpa": 9.7}
}
cgpas = {k: v["cgpa"] for k, v in students.items()}
print("MAX CGPA:", max(cgpas.values()))
print("MIN CGPA:", min(cgpas.values()))
print("AVERAGE:", sum(cgpas.values()) / len(cgpas))
print("All > 9?:", all([g > 9 for g in cgpas.values()]))

print("\nSorted:")
for name in sorted(students):
    print(f"{name}: {students[name]['major']}, {students[name]['cgpa']}")
