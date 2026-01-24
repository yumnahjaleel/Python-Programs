Reverse an Integer Without Using Strings
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
  
# Logic: Digit extraction using modulo/division
