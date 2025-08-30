inputString = str(input())
Apple = "apple"
Banana = "banana"
Grape = "grape"
Blueberry = "blueberry"
Orange = "orange"
resultList = []
fList = [Apple,Banana,Grape,Blueberry,Orange]
for f in fList:
    listF = f
    # listF = list(f)
    if inputString == listF[2] or inputString == listF[3]:
        resultList.append(f)
for result in resultList:
    print(result)
print(len(resultList))