h, w = map(int,input().split())

def bmi(h,w):
    return int((10000 * w) / pow(h,2))
result = bmi(h,w)
print(f"{result}")
if result >= 25:
    print("Obesity")
