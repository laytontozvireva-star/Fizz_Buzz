number = int(input("Enter number: "))
divisor = int(input("Enter divisor: "))
#function that returns a boolean

def is_divisible(number , divisor):
    return number % divisor == 0
#function that uses first function to ruturn fizz buzz fizzbuzz
def Fizz_Buzz_logic(n):
    if is_divisible(n, 3) and is_divisible (n, 5):
       return"FizzBuzz"
    elif is_divisible (n, 5) :
        return"Buzz"
    elif is_divisible (n, 3):
        return"Fizz"
    else:
        return(n)
for i in range (1,61):
    print(Fizz_Buzz_logic(i))



#quetion 2
def sum_digits(n):
    while n >=10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n
print(sum_digits(999))



