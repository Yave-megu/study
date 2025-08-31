A,B = map(int,input().split())
resultList = []
while A<=B:
    if A%2 == 1:
        resultList.append(A)
        A *= 2
    else:
        resultList.append(A)
        A += 3
for result in resultList:
    print(result, end = ' ')
    