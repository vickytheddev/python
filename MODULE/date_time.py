import datetime
x=datetime.datetime.now()
print(x)

y=datetime.datetime(2025,1,1)
print(y)

a=x.strftime("%y")  #year sort 25
print(a)
a=x.strftime("%Y")  #year full 2025
print(a)
a=x.strftime("%m")  #month 0-12
print(a)
a=x.strftime("%M")  #minute 00-59
print(a)
a=x.strftime("%b")  #month name sort Dec
print(a)
a=x.strftime("%B")  #month name full December
print(a)
a=x.strftime("%I")  #hour 00-12
print(a)
a=x.strftime("%H")  #hour 00-24
print(a)
a=x.strftime("%p")  #AM/PM
print(a)