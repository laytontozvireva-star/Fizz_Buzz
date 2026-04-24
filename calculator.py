#asking for inputes
a = int(input("Enter number: "))
opp = input("Enter opperator between ('-', '+', '*', '/'): ")
b = int(input("Enter number: "))

# function deals with addition
def add (a , b):
  if opp == '+':
    print(a + b)
 




#function that deals with subtration
def sub (a , b):
  if opp == '-':
    print (a - b)
 



#function that deals with multiplication
def mult (a , b):
   if opp == '*':
    print (a * b)
  


#the function that deals with division
def divisible(a ,b):
 try:
   if opp == '/':
    print (a / b)
 except ZeroDivisionError:
  print("can't devide  by zero")
  
   
add(a,b)
sub(a,b)
mult(a,b)
divisible(a,b)
    