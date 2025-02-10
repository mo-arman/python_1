luke_skills = {'Python', 'Java', 'SQL', 'R'}

print(luke_skills)

luke_skills.add('Excel')    
print(luke_skills)  # Output: {'R', 'Java', 'SQL', 'Python', 'Excel'}   

# luke_skills[2]

# luke_skills.append('Excel')  # AttributeError: 'tuple' object has no attribute 'append'

lukes_skill = ('p','s','t','st')
print(lukes_skill)  # Output: ('p', 's', 't', 'st')
new_skills = ('r','t','s','p')
print(new_skills)  # Output: ('r', 't', 's', 'p')

lukes_skill = lukes_skill + new_skills
print(lukes_skill)  # Output: ('p', 's', 't', 'st', 'r', 't', 's', 'p')
  
print(id(lukes_skill))  # Output: 140715000000640
print(id(new_skills))  # Output: 140715000000640

lukes_skill += new_skills
print(lukes_skill)  # Output: ('p', 's', 't', 'st', 'r', 't', 's', 'p', 'r', 't', 's', 'p')

print(id(lukes_skill))  # Output: 140715000000640
print(id(new_skills))  # Output: 140715000000640