First,Second = map(int,input().split())
tempList = [First,Second]
while len(tempList) != 10:
    length = len(tempList)
    newNumber = tempList[length-2] + tempList[length-1]
    while newNumber >=10:
        newNumber = newNumber%10
    result = newNumber
    tempList.append(result)
for i in tempList:
    print(i,end = ' ')