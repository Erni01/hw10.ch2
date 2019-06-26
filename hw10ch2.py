# 10. In mathematics, the factorial of an integer n, denoted by n! is the following product: n!=1×2×…×n
# For the given integer n calculate the value n!. Don't use math module in this exercise.


n = int(input("Enter the number: "))
factorial = 1

if n < 0:
    print("Negative numbers are not allowed for a factorial.")
if n == 0:
    print("1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i

print(factorial)