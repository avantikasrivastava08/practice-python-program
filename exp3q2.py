n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** digits
    temp //= 10

if sum_val == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
