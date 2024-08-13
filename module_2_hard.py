import random


def increase_pair(i, j):
    if i > j:
        return [j, i]
    else:
        return [i, j]


firstNum = random.randint(3, 20)
passwordList = []

for i in range(1, 19):
    for j in range(2, 19):
        if (firstNum % (i + j) == 0 and not passwordList.__contains__(increase_pair(i, j))) and not (firstNum == i+j and i == j):
            passwordList.append(increase_pair(i, j))

result = ""
for i in passwordList:
    for j in i:
        result += str(j)

print(firstNum)
print(result)
