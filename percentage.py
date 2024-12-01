mark1 = int(input("Enter your 1 subject marks "))
mark2 = int(input("Enter your 2 subject marks "))
mark3 = int(input("Enter your 3 subject marks "))

Total_percentage = (100*(mark1 + mark2 +mark3)) /300

if(Total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("congratulations 🎉 you passed" , Total_percentage)
else:
    print("Fail, better Luck next time!" , Total_percentage)