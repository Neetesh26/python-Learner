n = int(input("enter digitfor reverse : "))
newNum =0 
for i in range(len(str(n))):
    digit = n%10
    newNum = newNum *10 + digit
    n = n//10

print(f"converted : {newNum}")