liste = open('cal.txt', 'r')
sum1 = 0
sum2 = 0
for item in liste.readlines():
    part1, part2 = item.replace('\n', ''). split(',')
    part1 = part1.split('-')
    part2 = part2.split('-')
    
    #SOLUTION FOR A1
    if int(part1[1]) >= int(part2[1]) and int(part1[0])<=int(part2[0]): #SOLUTION FOR 4.1
        sum1 += 1
    elif int(part2[1]) >= int(part1[1]) and int(part2[0])<=int(part1[0]):
        sum1 += 1
    
    #SOLUTION FOR A2
    if int(part1[0]) <= int(part2[1]) and int(part1[1]) >= int(part2[0]):
            sum2 += 1
    elif int(part2[0]) <= int(part1[1]) and int(part2[1])>= int(part1[0]):
            sum2 += 1
            
print('A1: ' + str(sum1) + '\nA2: ' + str(sum2))
