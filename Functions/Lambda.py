def add_number(a,b):
    # Main Body
    result = add_number(5,3)
    print(result)


# Lambda Function

# Syntax lambda argument: expression

add = lambda a,b:a+b
print(add(5,7))

# Use with map()

numbers = [1,2,3,4,5,6]
squared = list(map(lambda x:x**2, numbers))
print(squared)

# use with Filter()

numbers = [1,2,3,4,5,6]
even_number = list(filter(lambda x: x%2 == 0, numbers))
print(even_number)
    
# Using With Sorted()

students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
