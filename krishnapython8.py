'''
python program to determine the entry ticket fare in a zoo
'''
age=int(input("enter your age:"))
if age<10:
    print("fare=7:")
elif age>=10 and age<60:
    print("fare=10:")
else:
    age>=60
    print("fare=5")
