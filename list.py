

# lists are mutable it means change the list values


friends =["apple" , "banana" , "neetesh", "boy" , "girl"]
print(friends[0])

friends[2] = "watermelon"
print(friends)

num = [1,5,8,9,5,6,6,8,88,99,9,5444,55,55,]

# num.sort()-----sort() fun

# num.reverse() -----

# num.insert(4 , 2626)
num.pop()   # num.pop(2) particular index remove or first value rmv
returnval = num.pop()
print(returnval)
print(num)
print(friends)


l = input("enter your name ")

if(l in friends):
    print("your name in list")
else:
    print("not available in list")