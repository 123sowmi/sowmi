
year=int(input("enter year to be checked:")) 
if year%4==0:
   if year%100==0: 
       if year%400==0: 
         print("the year is leap year!")
       else:
         print("the leap year is not a leap year!")
   else: 
       print("The year is a leap year!")
else:
  print("The year is not a leap year!")
  