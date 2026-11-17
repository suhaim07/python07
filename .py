reverse = 0
n = 123214
original = n

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if (original == reverse):
    print("palindrome")
else:
    print("not palindrome")