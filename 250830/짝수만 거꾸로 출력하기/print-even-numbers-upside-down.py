N = int(input())
numList = list(map(int,input().split()))
evenList = []
for num in numList:
    if num%2 == 0:
        evenList.append(num)
evenList.reverse()
for even in evenList:
    print(even, end = ' ')