Y = int(input())
Result = ""
if Y%4 == 0:
    Result = "true"
    if Y%100 == 0 and Y%400 != 0:
        Result = "false"
else:
    Result = "false"
print(Result)