import pandas as pd
import numpy as np
import calendar
import datetime

# Calculation for 5 day on weekday and 0.5 on weekend(saturday) working day
def workingDayCalc1(date,holidayDate=0):
  splitCurrentPeriode=date.split("-")
  sy=splitCurrentPeriode[0]
  sm=splitCurrentPeriode[1]
  mr=calendar.monthrange(int(sy),int(sm))

  sdObject=datetime.datetime.strptime(date+"-"+str("1"),"%Y-%m-%d")
  edObject=datetime.datetime.strptime(date+"-"+str(mr[1]),"%Y-%m-%d")
  
  sd=np.datetime64(sdObject.date())
  
  edObject_inclusive = edObject + datetime.timedelta(days=1)
  ed_inclusive = np.datetime64(edObject_inclusive.date())

  holidayList = []
  
  if holidayDate and holidayDate.strip() != "0":
    splithDay = [int(i) for i in holidayDate.split(",") if i.strip().isdigit()]
    for day in splithDay:
      formatted_date = f"{date}-{day:02d}"
      holidayList.append(formatted_date)

  wd = np.busday_count(sd, ed_inclusive,weekmask='1111100', holidays=holidayList)
  dates=np.arange(sd,ed_inclusive,dtype="datetime64[D]")

  we = sum(
    1 for d in dates if datetime.date.fromisoformat(str(d)).weekday() == 5
  )

  totalWorkingDay=(we*0.5)+wd
  return totalWorkingDay

# Calculation for 5 and 7 day working
def workingDayCalc2(date,holidayDate=0):
  splitCurrentPeriode=date.split("-")
  sy=splitCurrentPeriode[0]
  sm=splitCurrentPeriode[1]
  mr=calendar.monthrange(int(sy),int(sm))

  sdObject=datetime.datetime.strptime(date+"-"+str("1"),"%Y-%m-%d")
  edObject=datetime.datetime.strptime(date+"-"+str(mr[1]),"%Y-%m-%d")
  
  sd=np.datetime64(sdObject.date())
  
  edObject_inclusive = edObject + datetime.timedelta(days=1)
  ed_inclusive = np.datetime64(edObject_inclusive.date())

  holidayList = []
  
  if holidayDate and holidayDate.strip() != "0":
    splithDay = [int(i) for i in holidayDate.split(",") if i.strip().isdigit()]
    for day in splithDay:
      formatted_date = f"{date}-{day:02d}"
      holidayList.append(formatted_date)

  # If workdays occur every day and are only missed due to public holidays set weekmask to 1111111
  wd = np.busday_count(sd, ed_inclusive,weekmask='1111100', holidays=holidayList)

  totalWorkingDay=wd
  return totalWorkingDay

if __name__=="__main__":
  # Date in YYYY-MM format or set with datetime package by write down datetime.datetime.now().strftime("%Y-%m")
  # Set Holiday date in list format (e.g. ("17","18"))
  
  print(workingDayCalc1("2026-08",("17")))
  print(workingDayCalc2("2026-08",("17")))