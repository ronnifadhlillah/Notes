# LAMBDA'S EXAMPLE
from functools import reduce
import math
import pandas as pd

# TERNARY OPERATOR
# Using if else with lambda
# Using modulus to detect even or odd on number
oddEven=lambda x:"Even" if x % 2==0 else "Odd"
print(oddEven(4))

# Nested ternary
poin=lambda poin:("a" if poin>=85 else ("b" if poin >=70 and poin <=84 else("c" if poin >=60 and poin <=69 else "d")))
print("Result poin : "+poin(67))

# Dispatcher pattern
# Calculate the square if the number is positive, or the absolute square root if it is negative. 0=positive
number=lambda x: (x ** 2) if x >= 0 else math.sqrt(abs(x))
print(number(2)) # Result 4
print(number(0)) # Result still 0
print(number(-2)) # result 1.4142135....

# Ternary combination with map(),filter(),reduce()
nl = [-5, 12, 0, 8, -3, 20]

# If the number is less than 0, change it to 0. If it is even, divide by 2. If it is odd, multiply by 3
processNlMap1 = list(map(lambda x: 0 if x < 0 else (x // 2 if x % 2 == 0 else x * 3),nl))
print(processNlMap1) # Result [0, 6, 0, 4, 0, 10]

# Squaring the number
processNlMap2=list(map(lambda x: x**2,nl))
print(processNlMap2) # Result [25, 144, 0, 64, 9, 400]

# Get odd number
processNlFilter=list(filter(lambda x:x % 2==0, nl))
print(processNlFilter) # Result [12, 0, 8, 20]

# Sum all element
processNlReduce=reduce(lambda x,y: x+y,nl)
print(processNlReduce) # Result 32


# ======================================================================================================================

# LAMBDA IN REALWORLD
# There are various status of output within a process.
# In this case, we're want to adjust status classification become released and reject using lambda function
arr=[
  {"id":"1","name":"productA","qty":"1500","uom":"Kgs","status":"Released"},
  {"id":"2","name":"productB","qty":"800","uom":"Kgs","status":"Rejected"},
  {"id":"3","name":"productD","qty":"144","uom":"Kgs","status":"Rework"},
  {"id":"4","name":"productC","qty":"1766","uom":"Kgs","status":"Hold"},
  {"id":"5","name":"productE","qty":"1653","uom":"Kgs","status":"Bypass"},
  {"id":"6","name":"productC","qty":"989","uom":"Kgs","status":"Released"},
  {"id":"7","name":"productA","qty":"987","uom":"Kgs","status":"Released"},
  {"id":"8","name":"productD","qty":"346","uom":"Kgs","status":"Rework"},
  {"id":"9","name":"productB","qty":"768","uom":"Kgs","status":"Rework"},
  {"id":"10","name":"productB","qty":"1233","uom":"Kgs","status":"Bypass"},
  {"id":"11","name":"productA","qty":"1453","uom":"Kgs","status":"Released"}
]

# Set Released and bypass status become "Released"
# Set Reject, Hold, Rework status become "Rejected"

arrDf=pd.DataFrame(arr)
getRelease=arrDf[arrDf["status"].isin(["Released","Bypass"])]["id"].unique()
getReject=arrDf[arrDf["status"].isin(["Hold","Rejected","Rework"])]["id"].unique()
# Separating between release and reject status after classification
arrDf["statusChange"]=arrDf.apply(lambda x:"Released" if x["id"] in getRelease else ("Rejected" if x["id"] in getReject else x["id"]),axis=1)
print(arrDf.head(12))
# Result should be
#     id      name   qty  uom    status statusChange
# 0    1  productA  1500  Kgs  Released     Released
# 1    2  productB   800  Kgs  Rejected     Rejected
# 2    3  productD   144  Kgs    Rework     Rejected
# 3    4  productC  1766  Kgs      Hold     Rejected
# 4    5  productE  1653  Kgs    Bypass     Released
# 5    6  productC   989  Kgs  Released     Released
# 6    7  productA   987  Kgs  Released     Released
# 7    8  productD   346  Kgs    Rework     Rejected
# 8    9  productB   768  Kgs    Rework     Rejected
# 9   10  productB  1233  Kgs    Bypass     Released
# 10  11  productA  1453  Kgs  Released     Released

# Calculating output quantity by statusChange column
arrDf["qty"]=arrDf["qty"].astype(float)
totalSum=arrDf.groupby(lambda x:"Released" if arrDf.loc[x,"id"] in getRelease else ("Rejected" if arrDf.loc[x,"id"] in getReject else "Others"))["qty"].sum()
print(totalSum)
# Result : 
# Rejected    3824.0
# Released    7815.0

# USING LAMBDA IN DICTIONARY
# Dictionary contain simple math calc
opr = {
    'plus': lambda a, b: a + b,
    'minus': lambda a, b: a - b,
    'multiply': lambda a, b: a * b,
    'divide': lambda a, b: a / b if b != 0 else "Error: divide by zero"
}

print(opr["plus"](2,3)) # Result 5
print(opr["divide"](2,2)) # Result 1




