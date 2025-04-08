A,B = input().split()
A = int(A)
B = int(B)
result0 = 1
result1 = 1
if A<B :
    result0 = 1
else:
    result0 = 0
if A ==B:
    result1 = 1
else:
    result1 = 0
print(f"{result0} {result1}")