count = 0
n = int(input("Enter : "))

while n > 0:
    digit = n % 10
    count += 1
    n = n // 10

print(count) 