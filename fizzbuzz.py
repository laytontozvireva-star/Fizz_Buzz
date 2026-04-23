# number = int(input("Enter number: "))
# divisor = int(input("Enter divisor: "))

# #function that returns a boolean
# def is_divisible(number , divisor):
  
#   if number % divisor ==0:
#     return True
#   else:
#     return False
# print(is_divisible)
# is_divisible(number,divisor)


#     for m in range(1):
#        print (is_divisible(m))
#        is_divisible(number,divisor)

                                 
# #function that uses first function to ruturn fizz buzz fizzbuzz
# def Fizz_Buzz_logic(n):
#     if is_divisible(n, 3) and is_divisible (n, 5):
#        return"FizzBuzz"
#     elif is_divisible (n, 5) :
#         return"Buzz"
#     elif is_divisible (n, 3):
#         return"Fizz"
#     else:
#         return(n)
# for i in range (1,61):
#      print(Fizz_Buzz_logic(i))





# opp = input("Enter opperator: ")
# a = int(input("Enter number: "))
# b = int(input("Enter number: "))

# #adition function
# def calc (a, b):
#   if opp == '+':
#     print(a + b)
#   elif opp == '-':
#     print(a-b)
#   elif opp == '*':
#     print(a * b)
#   else:
#     print(round(a / b))
# calc (a, b)





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
  print("can devide  by zero")
divisible(a ,b)  
   
add(a,b)
sub(a,b)
mult(a,b)
divisible(a,b)
    