A,B = map(str,input().split())
if len(A) == len(B):
    print("same")
elif len(A)>len(B):
    print("{} {}".format(A,len(A)))
elif len(A)<len(B):
    print("{} {}".format(B,len(B)))