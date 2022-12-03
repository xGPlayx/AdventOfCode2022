liste = open('cal.txt', 'r')
arr1, arr2, setOf3 = [], [], []

for i in liste.readlines():
    if len(setOf3) == 2: #Aufgabe 2
        for j in i:
            if j in setOf3[0] and j in setOf3[1]:
                arr2.append(j)
                setOf3 = []
                break;
    else:
        setOf3.append(i)
    for j in i[0:len(i) // 2]: #Aufgabe 1
        if j in i[len(i) // 2:]:
            arr1.append(j)
            break;

def getSum(arr): #
    sum = 0
    for k in arr:
        if ord(k) > 90:
            sum += ord(k) - 96
        else:
            sum += ord(k) - 64 + 26
    return sum
print("Aufgabe 1: " + str(getSum(arr1)))
print("Aufgabe 2: " + str(getSum(arr2)))
