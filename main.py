monthDays = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
def piday(name, month, day, year):
  currentDay = 0
  piDay = 73
  if month == "january":
    currentDay = monthDays[0] + day
  elif month == "february":
    currentDay = monthDays[1] + day
  elif month == "march":
    currentDay = monthDays[2] + day
  elif month == "april":
    currentDay = monthDays[3] + day
  elif month == "may":
    currentDay = monthDays[4] + day
  elif month == "june":
    currentDay = monthDays[5] + day
  elif month == "july":
    currentDay = monthDays[6] + day
  elif month == "august":
    currentDay = monthDays[7] + day
  elif month == "september":
    currentDay = monthDays[8] + day
  elif month == "october":
    currentDay = monthDays[9] + day
  elif month == "november":
    currentDay = monthDays[10] + day
  elif month == "december":
    currentDay = monthDays[11] + day
  while currentDay != piDay:


#take user input
#call function and pass input
