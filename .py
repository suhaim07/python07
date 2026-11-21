terms = int(input("How many terms? "))
first = 0
second = 1

if terms <= 0:
    print("Enter a positive number of terms.")
else:
    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second
    print()
