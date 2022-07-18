print("Enter A Number:")
num = int(input())
if num % 2 == 0 and 2 > num < 5:
    print("Not Weird")
elif num % 2 == 0 and 6 > num < 20:
    print("Weird")
elif num % 2 == 0 and num > 20:
    print("Not Weird")
else: 
    print("Weird")


'''print("Enter A Number:")
num = int(input())
if num % 2 != 0:
    print("Weird")
elif num % 2 == 0 and 2 > num < 5:
    print("Not Weird")
elif'''
