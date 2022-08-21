



#ruuning a code for MTN MONO.....loading
code=input("please enter your code: ")
if code=="*170#":
    print("(1)Transfer money\n(2)Momo pay& pay bill\n(3)Airtime& Bundle\n(4)Allow cash out\n(5)Finacial services\n(6)My wallet")
    option=input("Enter choice: ")
    
    if option=="1":
        print("(1)Momo user\n (2)Non momo user\n (3)Send with care\n(4)Favourite\n(5)other network")
        option=input("Enter choice: ")
        
        if  option =='1':
            option=int(input("Enter a mobile number: "))
            options=int(input("Please Confirm your number: "))
            while (option==1):
                Entry = float(input("Enter amount of your choice(1-200):"))
                print('your amount is',Entry )
                confirm=input("please enter 1 to confirm:",option)
                print('Your information is in process please wait for 2 minute')
                print("please try again::")
            
        
if option=="2":
    print("(1) Momopay\n (2)Paybill\n (3)GHQR\n (4)Back")
    option=input("Enter choice: ")
        
    if option=="3":
        print("(1) Airtime\n (2)Internet bundle\n (3)fixed bundle\n (4)schdule bundle\n (5) Back")
        option=input("Enter choice: ")

        
        
else:
    print("wrong input code please try again:")



                #First option Ends#  
