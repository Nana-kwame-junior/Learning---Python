n=int(input("enter number from 1 to 100 :"))

if n%2==0:
    print(" weird")
elif n%2==0 and range(2,5):
    print ("not weird")
elif n%2==0 and range(6,25):
    print("weird")
elif n%2==0 and n<20:
    print("weird")
else:
    print("not weird")


