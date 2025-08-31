N = int(input())
inputData = []
for i in range(N):
    inputData.append(list(map(int,input().split())))

for i,j in inputData:
    evenSum = 0
    for x in range(i,j+1):
        if x%2 ==1:
            continue
        else:
            evenSum += x
    print(evenSum)