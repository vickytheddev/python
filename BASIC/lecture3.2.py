list=[1,2,3,2,1]
copylist=list.copy()
copylist.reverse()
if(list==copylist):
    print("palindrome")
else:
    print("not palindrome")