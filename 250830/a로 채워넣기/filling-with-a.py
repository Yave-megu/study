inputString = list(input())
inputString[1] = 'a'
inputString[len(inputString)-2] = 'a'
for i in inputString:
    print(i,end = '')