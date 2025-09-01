N = int(input())

for j in range(N):
    row = []
    for i in range(1,N+1):
        row.append(i)
    if j%2 == 0:
        for i in range(N):
            print(row[i],end="")
    else:
        row.reverse()
        for i in range(N):
            print(row[i],end="")
    print()