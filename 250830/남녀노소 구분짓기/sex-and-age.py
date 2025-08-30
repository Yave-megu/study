Gender = int(input())
Age = int(input())

if Gender == 0:
    if Age >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if Age >= 19:
        print("WOMAN")
    else:
        print("GIRL")