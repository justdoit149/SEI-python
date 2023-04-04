from datetime import datetime 

CurrentAge = int(input("What is your current age?"))
RetireAge = int(input("At what age would you like to retire?"))
years = RetireAge - CurrentAge
CurrentYear = datetime.now().year   #获取当前时间，并截取出年份
print("You have {} years left until you can retire.".format(max(years,0)))#注意可能当前年龄大于退休年龄
print("It's {}, so you can retire in {}.".format(CurrentYear, CurrentYear + years))
