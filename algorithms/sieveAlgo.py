
# def sieve(num):
#     isPrime =  [True for i in range(num +1)]
    
#     p = 2
#     while p*p < num:
#         if (isPrime[p]):
#             for i in range(p*p,num+1,p):
#                 isPrime[i] =False
#         p +=1

#     result = [i for i in range(num+1) if (isPrime[i])]
#     return result 
# print(sieve(20))


def sieve(n):
    isPrime = [ True for i in range(n+1)]

    p  = 2 

    while p*p < n:
        if(isPrime[p]):
            for i in range(p*p,n+1,p):
                isPrime[i] = False
        p +=1
    result = [i for i in range(n+1) if(isPrime[i])]
    return result 



print(sieve(20))