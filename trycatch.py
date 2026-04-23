#function that deals with division

a = int(input("Enter number: "))
opp = input("Enter opperator between ('-', '+', '*', '/'): ")
b = int(input("Enter number: "))
def divisible(a ,b):
 try:
   if opp == '/':
    print (a / b)
 except ZeroDivisionError:
  print("can devide  by zero")
divisible(a ,b) 
