N, M = map(int, input().split())

# Please write your code here.
print(N)
while N>M:
    result = N/M
    print(int(result))
    N = result