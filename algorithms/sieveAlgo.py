
def sieve(num):
    isPrime =  [True for i in range(num +1)]
    
    p = 2
    while p*p < num:
        if (isPrime[p]):
            for i in range(p*p,num+1,p):
                isPrime[i] =False
        p +=1

    result = [i for i in range(num+1) if (isPrime[i])]
    return result 
print(sieve(20))