A,B = map(int,input().split())
numSum = 0
for i in range(A,B+1):
    if i%2 ==1:
        continue
    numSum += i
print(numSum)