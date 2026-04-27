# def isfibo(n):
#     if n<=1:
#         return n
#     return isfibo(n-1) + isfibo(n-2)


# print(isfibo(4))

def isfibo(n,a=0, b=1):
    if n <=0:
        return 
    print(a,end=" ")
    return isfibo(n-1,b,a+b)

isfibo(5)