Score = int(input())
while Score <= 100:
    if Score >= 90:
        print("A",end=" ")
        Score += 1
    elif Score>=80:
        print("B",end=" ")
        Score += 1
    elif Score>=70:
        print("C",end=" ")
        Score += 1
    elif Score>=60:
        print("D",end=" ")
        Score += 1
    else:
        print("F",end=" ")
        Score += 1
    