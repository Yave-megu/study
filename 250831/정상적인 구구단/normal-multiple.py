N = int(input())
for j in range(1,N+1):
    for i in range(1,N+1):
        comma =", "
        newline = "\n"
        if i == N:
            print(f"{j} * {i} = {j*i}",end = newline)
        else:
            print(f"{j} * {i} = {j*i}",end = comma)