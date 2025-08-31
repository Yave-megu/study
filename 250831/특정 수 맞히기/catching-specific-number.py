while True:
    numInput = int(input())
    if numInput > 25:
        print("Lower")
        continue
    elif numInput < 25:
        print("Higher")
        continue
    else:
        print("Good")
        break;