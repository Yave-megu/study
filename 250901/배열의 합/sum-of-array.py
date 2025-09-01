inputMatrix = []
for i in range(4):
    inputMatrix.append(list(map(int,input().split())))
for j in range(4):
    cnt = 0
    cnt = sum(inputMatrix[j])
    # for i in range(4):
    #     cnt += inputMatrix[j][i]
    print(cnt)