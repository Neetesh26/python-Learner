# num = int(input("Enter a number: "))
# for i in range(num):
#     for j in range(num):
#         print("* ", end="")
#     print()  # Move to the next line after each row



def print2():
    n= int(input())

    for i in range(n):
        for j in range(0,i):
            print(i)
        print()

print2()