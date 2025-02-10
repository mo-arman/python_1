job_skills = {'Python', 'Java', 'SQL', 'R'}
print(len(job_skills))  # Output: 4
print(job_skills)  # Output: {'R', 'Java', 'SQL', 'Python'}

analyst_list = ['python']

for job in job_skills:
    analyst_list.append(job)
    print(analyst_list)

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

char = 'Data Nerds'

for charc in char:
    print(charc)

years_expericence = {
    'Alice': 16, 'Bob': 19, 'Charlie': 27, 'David': 2, 'Emma': 16,
    'Frank': 14, 'Grace': 29, 'Henry': 23, 'Ivy': 5, 'Jack': 27,
    'Katie': 1, 'Liam': 21, 'Mia': 25, 'Noah': 7, 'Olivia': 14,
    'Paul': 4, 'Quinn': 19, 'Ryan': 27, 'Sophia': 21, 'Tom': 5,
    'Uma': 27, 'Victor': 17, 'Wendy': 10, 'Xavier': 8, 'Yasmine': 22
}

print(years_expericence)

print(years_expericence.keys()) 

for person in years_expericence:
    print(person)

for value in years_expericence.values():
    print(value)

for itme in years_expericence.items():
    print(itme)

for key,value in years_expericence.items():
    if value > 20:
        print(key,'has',value,'years of experience')

for tp in range(30):
    print(tp)