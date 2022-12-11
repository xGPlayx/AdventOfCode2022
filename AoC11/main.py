from decimal import Decimal
import datetime
liste = open('itscalagain.txt', 'r')
devisor = [3, 13, 19, 17, 5, 7, 11, 2]
monkeys = []

def is_multiplication(symbol):
    return symbol == '*'

def is_devisable(number):
    global devisor
    devisable = []
    for dev in devisor:
        devisable.append(number % dev)
    return devisable

def monkey_inspect(monkey):
    global monkeys
    global devisor
    for item in monkey[0]:
        monkey[5] += 1
        mult = is_multiplication(monkey[1][0])
        old = (monkey[1][1] == 'old')
        result = []
        for index, value in enumerate(item):
            if mult and old:
                result.append((value * value) % devisor[index])
            elif mult:
                result.append((value * int(monkey[1][1])) % devisor[index])
            else:
                result.append((value + int(monkey[1][1])) % devisor[index])
        if result[devisor.index(monkey[2])] == 0:
            monkeys[monkey[3]][0].append(result)
        else:
            monkeys[monkey[4]][0].append(result)
    monkey[0] = []

""" #AUFGABE 1
def monkey_inspect(monkey):
    global monkeys
    for item in monkey[0]:
        monkey[5] += 1
        value = 0
        if is_multiplication(monkey[1][0]):
            if monkey[1][1] == 'old':
                value = int(item) * int(item)
            else:
                value = int(item) * int(monkey[1][1])
        else:
            value = int(item) + int(monkey[1][1])
        value = int(value / 3)
        if value % monkey[2] == 0:
            monkeys[monkey[3]][0].append(value)
        else:
            monkeys[monkey[4]][0].append(value)
    monkey[0] = []

for item in liste.readlines():
    if item.startswith("Monkey"):
        monkeys.append([])
    elif item.startswith("  Starting"):
        monkeys[len(monkeys)-1].append(item.replace("\n", '').split(": ")[1].split(", "))
    elif item.startswith("  Operation:"):
        monkeys[len(monkeys)-1].append(item.replace("\n", '').split("= ")[1][4:].split(" "))
    elif item.startswith("  Test:"):
        monkeys[len(monkeys)-1].append(int(item.replace('\n', '').split(' ')[5]))
    elif item.startswith("    If true:"):
        monkeys[len(monkeys)-1].append(int(item[len(item)-2:]))
    elif item.startswith("    If false:"):
        monkeys[len(monkeys)-1].append(int(item[len(item)-2:]))
"""

for item in liste.readlines():
    if item.startswith("Monkey"):
        monkeys.append([])
    elif item.startswith("  Starting"):
        monkeys[len(monkeys)-1].append([])
        for value in item.replace("\n", '').split(": ")[1].split(", "):
            monkeys[len(monkeys)-1][0].append(is_devisable(int(value)))
    elif item.startswith("  Operation:"):
        monkeys[len(monkeys)-1].append(item.replace("\n", '').split("= ")[1][4:].split(" "))
    elif item.startswith("  Test:"):
        monkeys[len(monkeys)-1].append(int(item.replace('\n', '').split(' ')[5]))
    elif item.startswith("    If true:"):
        monkeys[len(monkeys)-1].append(int(item[len(item)-2:]))
    elif item.startswith("    If false:"):
        monkeys[len(monkeys)-1].append(int(item[len(item)-2:]))

for monkey in monkeys:
    monkey.append(0)

for _ in range(10000):
    for monkey in monkeys:
        monkey_inspect(monkey)

result = [0, 0]
for monkey in monkeys:
    if monkey[5] > result[0]:
        result[0] = monkey[5]
        result.sort()

print(result[0] * result[1])
