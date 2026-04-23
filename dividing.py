
#quetion 2
def sum_digits(n):
    while n >=10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n
print(sum_digits(789))