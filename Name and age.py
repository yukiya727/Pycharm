import datetime

yy = input("What is your birth of year? :")
mm = input("What is your birth of month? :")
dd = input("What is your birth of day? :")

print(isinstance(yy, int))

yy = int(yy)
mm = int(mm)
dd = int(dd)

Time = datetime.datetime.now()

if mm >= Time.month and dd >= Time.day:
    age = Time.year - yy - 1
else: age = Time.year - yy

age100 = yy + 100
print("You will turn into 100 at the year of ", age100)
print(age)

