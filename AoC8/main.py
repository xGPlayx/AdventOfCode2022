liste = open('cal.txt', 'r')
trees = []
visible = []
res = []
for item in liste.readlines():
     trees.append(list(str(item).replace('\n','')))

for i in trees:
    vis = []
    for j in i:
        vis.append(True)
    visible.append(vis)

#Aufgabe 1
for idx, i in enumerate(trees):
    for jdx, j in enumerate(i):
        if (idx != 0 and idx != len(trees)-1) and (jdx != 0 and jdx != len(i)-1):
            isVisibleX = True
            isVisibleY = True
            isVisiblePlus = True
            isVisibleMinus = True
            for x in range(0, jdx):
                if int(trees[idx][jdx]) <= int(trees[idx][x]):
                    isVisibleMinus = False
            for x in range(jdx+1, len(i)):
                if int(trees[idx][jdx]) <= int(trees[idx][x]):
                    isVisiblePlus = False
            isVisibleX = isVisiblePlus or isVisibleMinus
            isVisibleMinus = True
            isVisiblePlus = True
            for y in range(0, idx):
                if int(trees[idx][jdx]) <= int(trees[y][jdx]):
                    isVisibleMinus = False
            for y in range(idx+1, len(trees)):
                if int(trees[idx][jdx]) <= int(trees[y][jdx]):
                    isVisiblePlus = False
            isVisibleY = isVisibleMinus or isVisiblePlus
            visible[idx][jdx] = isVisibleY or isVisibleX

sum = 0
for i in visible:
    sum += i.count(True)
print(sum)

#Aufgabe 2
for idx, i in enumerate(trees):
    for jdx, j in enumerate(i):
        if idx != 0 and idx != len(trees)-1 and jdx != 0 and jdx != len(i)-1:
            xm = jdx - 1
            xp = jdx + 1
            ym = idx - 1
            yp = idx + 1
            while xm > 0 and trees[idx][xm] < trees[idx][jdx]:
                xm -= 1
            disXM = jdx - xm
            while ym > 0 and trees[ym][jdx] < trees[idx][jdx]:
                ym -= 1
            disYM = idx - ym
            while xp < len(i) - 1 and trees[idx][xp] < trees[idx][jdx]:
                xp += 1
            disXP = xp - jdx
            while yp < len(trees) - 1 and trees[yp][jdx] < trees[idx][jdx]:
                yp += 1
            disYP = yp - idx
            res.append(disXP*disYM*disXM*disYP)

print(max(res))