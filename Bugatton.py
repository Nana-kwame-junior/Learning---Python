def findPrimeFactors(num):
    
    arr = [];

    for i in range(2,num):
       
        if num % i == 0:
            isPrime = True
       
            for j in range(2,i):
            
                if i % j == 0 :
                    isPrime == False
            

            if isPrime == True: 
                arr.append(i)

    return arr.__len__()
print(findPrimeFactors((7000)))
