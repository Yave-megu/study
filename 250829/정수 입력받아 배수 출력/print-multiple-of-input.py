N = int(input())
result = ""
for i in range(1,6):
    result += str(N * i) + " "
result.strip()
print(result)