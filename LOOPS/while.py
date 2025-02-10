count = 1
while count < 6:
    print(count)
    count += 1

years_experience = {
    'Alice': 16, 'Bob': 19, 'Charlie': 27, 'David': 2, 'Emma': 16,
    'Frank': 14, 'Grace': 29,
}

print(years_experience)

years = 0 
years_list = list(years_experience.items())

print(years_list)

print(years_list[2])


years = 0
index = 0

years_list = list(years_experience.items())

while years < 20:
    key,years = years_list[index]
    if years >= 5:
        print(key,'has',years,'years of experience')
        index += 1