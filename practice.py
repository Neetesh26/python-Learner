# i =0
# while i<=100:
#     print("value of i : " , i)
#     i+=1


    #practice 2

"""
number = int(input("Enter your number to find table : "))
i = 1
while i <=10:
    print(f'{number} * {i} = ',i* number)
    i+=1
"""

#question no 4
nums = [1,4,9,16,25,36,49,64,81,100]

i = 0

'''
while i < len(nums): 
    print(nums[i])
    i +=1

print("end program all element printed")
'''

# search element

userNum = int(input("enter your to search in list"))

while i < len(nums):
    if(nums[i] == userNum):
        print("available in list at index is : " , i)
        break
    else:
        print("finding...")
    i+=1
print("end loop")