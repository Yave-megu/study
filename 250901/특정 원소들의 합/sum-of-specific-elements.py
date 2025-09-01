Matrix = []
for i in range(4):
    Matrix.append(list(map(int,input().split())))
result = 0
for j in range(4):
    for i in range(4):
        if j>= i:
            result += Matrix[j][i]
print(result)