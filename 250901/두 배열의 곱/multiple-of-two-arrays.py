Matrix_1 = []
Matrix_2 = []

for i in range(3):
    Matrix_1.append(list(map(int,input().split())))
p = input()
for i in range(3):
    Matrix_2.append(list(map(int,input().split())))

for i in range(3):
    for j in range(3):
        result = Matrix_1[i][j] * Matrix_2[i][j]
        print(result, end = ' ')
    print()