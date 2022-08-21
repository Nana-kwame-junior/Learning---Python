import random
def draw():#draw session
    numbers=[]
    for i in range(0,5):
        if len(numbers)<5:
            numbers.append(random.randint(1,91))
    return numbers
    
#running a code for NLA#
code=input('enter code:')
if code == '*959#':#firts if
    print('(1)Monday special\n(2) Draw Results \n(3)Terms & condition read')#select option here
    option=input("Enter choice:")#input a choice for option
    
    if option =='1':#second if (display another menu)
        print('(1) Direct-1\n (2) sure\n (3) direct-3\n (4) direct-4\n (5)direct-5\n perm 3 or more')#choose from the menu
        option=input("Enter choice:")#choose a choice for option 2

        #Terms and conditions
    if option=='3':
        confirm=int(input("Please enter 1 to see our Terms and conditions: "))
        print("please find 5/9 from NLA terms and conditions on this link: http://590mobile.com.gh/tcs.php.. ")
        
        #Terms and  conditions
        
        #First option start#      
        if option=='1':
            Entry=int(input("Enter a number(1:90):"))
            if Entry in range(1,90):#choose a range 
                Entry = float(input("Enter amount(1-200):"))
                if Entry in range (1-200):
                    print('your amount is %.2f' % Entry)#end second if for option one 
                else:
                    confirm=input("please enter 1 to confirm: ")
                    print('Your information is in process please wait for 5 minute')
            else:
                print('wrong input')
                #First option Ends#  
                
                #two sure#
        elif option=='2':#secod if for option one start
            Entry=input("Enter your two sure numbers buddy:")
            Entry = float(input("Enter amount(1-200):"))
            if Entry in range (1-200):
                print('your amount is %.2f' % Entry)#end second if for option one 
            else:
                print('your amount is %.2f' % Entry)
                confirm=input("Enter 1 to confirm:")
                if confirm=="1":
                    print("Wahoo buddy you are amazing")
                else:
                    print("you need to pay buddy")
               
            
                #three direct end#
            if option=='3':#secod if for option one start
                Entry=input("Enter your three direct numbers buddy:")
                Entry = (input("Enter amount(1-200):"))
                if Entry in range (1-200):
                    print('your amount is %.2f' % Entry)#end second if for option one 
            else:
                confirm=input("Enter 1 to confirm:")
                if confirm=="1":
                    print("Wahoo buddy you are amazing")
                else:
                    print("you need to pay buddy")
                
            #three direct ends#
                    

    if option =='2':#third option  
        Entry=input("Enter your draw results: ")
        if Entry == draw():
               print(draw())
        else:
            print("you have lost", draw())#end third option

else:
    print("Invalid code input")#first if end
   


 
