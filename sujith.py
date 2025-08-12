print("vote age finder:")
age=int(input("Enter your age:"))
if(age<18):
    print("You gotta grow up!")
elif(age>=18 and age<=100):
    print("Yes you are eligibe fo voting!")
else:
    print("sorry buddy re-enter your age!")