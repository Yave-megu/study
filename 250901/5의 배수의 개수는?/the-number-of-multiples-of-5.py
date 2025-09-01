Matrix = []
for i in range(4):
    Matrix.append(list(map(int,input().split())))
cnt = 0
for j in range(4):
    for i in range(4):
        if Matrix[j][i]%5 == 0:
            cnt += 1
print(cnt)