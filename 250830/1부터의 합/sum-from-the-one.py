N = int(input())
numSum = 0
for i in range(1,101):
    numSum += i
    if numSum < N:
        continue
    else:
        print(i)
        break