liste = open('cal.txt', 'r')
sum = 0;
cur = []
for item in liste.readlines():
    for i in item:
        sum += 1
        if len(cur) == 14:
            cur.remove(cur[0])
        cur.append(i)
        if len(set(cur)) == 14:
            break;
    """ #SOLUTION FOR 1)
    for i in item:
        sum += 1
        if len(cur) == 4:
            cur.remove(cur[0])
        cur.append(i)
        if len(set(cur)) == 4:
            break;
    """
print(sum)