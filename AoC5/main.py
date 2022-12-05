liste = open('cal.txt', 'r')
answer = ''
arr = [['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'],
       ['H','F','R'],
       ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
       ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
       ['P', 'S', 'M', 'J', 'H'],
       ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
       ['P', 'T', 'H', 'N', 'M', 'L'],
       ['F', 'D', 'Q', 'R'],
       ['D', 'S', 'C', 'N', 'L', 'P', 'H']]

def move(count, start, end):
    element = []
    for i in range(0, count):
        element.append(arr[start-1].pop())
    arr[end-1] = arr[end-1] + element[::-1]
    """#SOLUTION FOR 1)
    for i in range(0, count):
        element = arr[start-1].pop()
        arr[end-1].append(element)
    """

for item in liste.readlines():
    tmp = item.split(' ')
    move(int(tmp[1]), int(tmp[3]), int(tmp[5]))

for i in arr:
    answer = answer + i.pop()
print(answer)