count = 0
n = int(input("Enter : "))

while n > 0:
    digit = n % 10
    count += digit
    n = n//10
print(count)