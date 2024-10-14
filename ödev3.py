
number=input("enter a number")
def func(x):
    if x%3==0:
       return True
    if x%5==0:
       return True
    else:
       return False
number=int(input("number"))
result=func(number)
elif result== True:
    print("divisible")
elif result== False:
    print("no")
