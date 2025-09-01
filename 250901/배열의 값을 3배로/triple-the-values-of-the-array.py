inputMatrix = []
for i in range(3):
    inputMatrix.append(list(map(int,input().split())))
for i in range(3):
    for j in range(3):
        inputMatrix[i][j] *= 3
        print(inputMatrix[i][j], end = ' ')
    print()
