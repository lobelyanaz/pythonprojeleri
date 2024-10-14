day=input("what is the day?")
def func(day):
    if day== saturday or sunday:
       return True
    else:
       return False

weekend=int(input("weekend"))
result=func(day)
if result== True:
   print("weekend")
if result== False:
   print("otherwise")
                
