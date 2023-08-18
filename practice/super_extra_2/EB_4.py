peopleA = 5e7
peopleB = 7e7
growthA = 0.03
growthB = 0.02
year = 0
while peopleA < peopleB:
    peopleA += peopleA * growthA
    peopleB += peopleB * growthB
    year += 1
print(year)
