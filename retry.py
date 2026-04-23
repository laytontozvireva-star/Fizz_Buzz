#function that deals with division

a = int(input("Enter number: "))
opp = input("Enter opperator between ('-', '+', '*', '/'): ")
b = int(input("Enter number: "))

try:
 def division (a , b):
   if opp == '/':
    print (a / b)
except ZeroDivisionError:
  print("division by zero") 
division(a,b)