number = int(input("Enter number: "))
divisor = int(input("Enter divisor: "))

#function that returns a boolean
def is_divisible(number , divisor):
    if number % divisor ==0:
     print("true")
    else:
       print("false")

is_divisible(number,divisor)