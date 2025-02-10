my_set = {1, 2, 3, 4, 5,}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)        # Adds an element
my_set.remove(2)     # Removes an element
print(my_set)  # Output: {1, 3, 4, 5, 6}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union → {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection → {3, 4}
print(A - B)  # Difference → {1, 2}
print(A ^ B)  # Symmetric Difference → {1, 2, 5, 6}

print(3 in A)   # Output: True
print(7 in A)   # Output: False


job_skills = {'Python', 'Java', 'SQL', 'R'}

print(job_skills)

# job_skills[2]  # Error: 'set' object does not support indexing

help(set) # Help on class set in module builtins

job_skills.add('Excel')
print(job_skills)  # Output: {'R', 'Java', 'SQL', 'Python', 'Excel'}

