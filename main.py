# print('hello neetesh broh')
# num =int(input("enter number "))
# print(num)

# if(num >= 100 and num < 0):
#     print("number is under the 0 to 100 ")




# n = int(input("Enter your num to find factors : "))
# sum = 0
# for i in range(1, (n//2)+1):
#     if(n%i==0):
#         print(i)
#         sum+=i
# print(f"sum of all factors number : {sum}")


# number is prime or not------------------>❓

n = int(input("Enter your number : "))
count =0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count == 2 ):
    print("number is prime. ")
else:
    print("number is not prime.")

    