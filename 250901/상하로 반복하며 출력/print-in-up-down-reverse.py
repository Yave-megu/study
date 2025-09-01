N = int(input())
result = []
for j in range(N):
    row = []
    for i in range(1,N+1):
        row.append(i)
    if j%2 == 0:
        row.reverse()
    result.append(row)
for j in range(N-1,-1,-1):
    for i in range(N):
        print(result[i][j],end = "")
    print()
