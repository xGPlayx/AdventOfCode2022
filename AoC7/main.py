liste = open('cal.txt', 'r')
dir =  {}
cd = ''
revdir = {}


def getSize(x):
    sum = 0
    if len(dir[x]) > 1:
        for index, i in enumerate(dir[x]):
            if index != 0:
                sum += getSize(i)
    sum += dir[x][0]
    return sum


for item in liste.readlines():
    cur = item.split(' ')
    if cur[0] == '$':
        if cur[1] == 'cd':
            if cur[2] == '..':
                cd = revdir[cd]
            else:
                revdir[cur[2]] = cd
                cd = cur[2][:-1]
                dir[cd] = [0]
    else:
        if cur[0] == 'dir':
            dir[cd].append(cur[1][:-1])
        else:
            dir[cd][0] += int(cur[0])

sizearr = []
for i in dir:
    if getSize(i) < 100000:
        sizearr.append(getSize(i))
solution = []

for index, i in enumerate(sorted(sizearr)[::-1]):
    j = len(sizearr) - index - 1
    sum = index
    curSum = i
    while j > index + 1:
        curSum += sorted(sizearr)[::-1][j]
        if curSum > 100000:
            solution.append(curSum - sorted(sizearr)[::-1][j])
            curSum = i
        j-=1


print(sorted(sizearr)[::-1])
print(sorted(solution)[::-1])
#[96517, 96517, 80731, 78613, 75203, 74576, 74576, 73403, 69506, 69285, 65797, 56213, 47983, 22219, 20979, 13067, 10603, 6278, 5610, 2762, 424, 424, 0]
