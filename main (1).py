#program to check whether the given year is leap year or not using if,elif and else

def isleapYear(year):
  if(year % 4 == 0 and year % 100 != 0):
    return True
  elif(year % 400 == 0):
    return True
  else:
    return False

year = int (input("Enter the year : "))
if(isleapYear(year)):
  print("{} is a leap year".format(year))
else:
  print("{} is not a leap year".format(year))