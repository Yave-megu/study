a,b = input().split()

a = int(a)
b = int(b)
if a>b:
    print(f"{a*b}")
else:
    print(f"{int(b/a)}")