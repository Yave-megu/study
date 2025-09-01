N = int(input())
a = 0
for i in range(N):
    for j in range(i+1):
        a += 1
        if j == i:
            print(a, end = "\n")
        else:
            print(a, end = " ")