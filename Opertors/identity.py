salary_kelly = 1000_000
salary_joe = 1000_00
print(salary_kelly is salary_joe) # False

print(id(salary_kelly) == id(salary_joe))  # Output: 140715000000640

print(id(salary_kelly))  # Output: 140715000000640
