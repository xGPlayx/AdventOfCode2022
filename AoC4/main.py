liste = open('cal.txt', 'r')
sum = 0
for item in liste.readlines():
    part1, part2 = item.replace('\n', ''). split(',')
    part1 = part1.split('-')
    part2 = part2.split('-')
    """if int(part1[1]) >= int(part2[1]) and int(part1[0])<=int(part2[0]):
        sum += 1
    elif int(part2[1]) >= int(part1[1]) and int(part2[0])<=int(part1[0]):
        sum += 1"""
    if int(part1[0]) <= int(part2[1]) and int(part1[1]) >= int(part2[0]):
            sum += 1
    elif int(part2[0]) <= int(part1[1]) and int(part2[1])>= int(part1[0]):
            sum += 1
print(sum)