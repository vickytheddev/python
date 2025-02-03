day=int(input("Enter the day: "))
if(day>0 and day<=5):
    fine=day*0.40
    print(fine)
elif(day>5 and day<=10):
    fine=day*0.65
    print(fine)
else:
    fine=day*0.80
    print(fine)