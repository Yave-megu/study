numList = []
for i in range(10):
    numList.append(int(input()))
thirdList = []
fivethList = []
for num in numList:
    if num % 3 == 0:
        thirdList.append(num)
    if num%5 == 0:
        fivethList.append(num)
print(f"{len(thirdList)} {len(fivethList)}")