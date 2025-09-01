start, end = map(int, input().split())
resultList = []
# Please write your code here.
for i in range(start,end+1):
    divisorList = []
    for j in range(1,i+1):
        if i%j == 0:
            divisorList.append(j)
    if len(divisorList) == 3:
        resultList.append(i)
print(len(resultList))
