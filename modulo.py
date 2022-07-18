n = int(input("Enter an integer between 1 to 100: "))
if n%2 != 0:
    print("weird")
elif n%2 == 0 and n >= 2 and n <= 5:
    print("Not weird")
elif n%2 == 0 and n >= 6 and n <= 20:
    print("Weird")
elif n%2 == 0 and n > 20 and n <= 100:
    print("Not weird")
else:
    print("Invalid input")
