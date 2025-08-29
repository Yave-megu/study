inputData = input()
A,B = inputData.split()
A = int(A)
B = int(B)
result = ""
for i in range(0,B-A+1):
    result += str(B-i) + " "
result.strip()
print(result)