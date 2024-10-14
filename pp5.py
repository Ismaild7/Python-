no_of_days=int(input())
year= no_of_days//365
week=(no_of_days%365)//7
days=(no_of_days%365)%7
print("years =",year,"weeks =",week,"days =",days)
