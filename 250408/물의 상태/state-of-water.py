water = "water"
ice = "ice"
vapor = "vapor"
temp = int(input())

if temp<0:
    print(ice)
elif temp >= 100:
    print(vapor)
else:
    print(water)