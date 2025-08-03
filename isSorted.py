# li = [56,5468,4,5,588,4,5,48,45,5,2,55]
li=[1,2,3,8,9,42,55,65]
for i  in range(len(li)-1):
    if(li[i]< li[i+1]):
        continue
    else:
        print("list is not sorted")
        break
else:
    print("list is sorted.")