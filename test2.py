# while True:
#     x = input("input:")
#     if type(x) == int:
#         print("int")
#         break
#     else:
#         print("try again")
x = input("input:")
x = int(x)

numof3 = x/3
numof5 = x/5
numof15 = x/15

total = x - numof3 - numof5 +2*numof15

print("output:"+str(total))