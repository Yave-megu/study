N,M = map(int,input().split())
inputMatrix = []
diffMatrix = []
for i in range(N):
    inputMatrix.append(list(map(int,input().split())))
for i in range(N):
    diffMatrix.append(list(map(int,input().split())))
for j in range(N):
    for i in range(M):
        if inputMatrix[j][i] == diffMatrix[j][i]:
            print("0", end = " ")
        else:
            print("1", end = " ")
    print()