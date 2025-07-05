def Show_Balance ():
    print("="*30)
    print("="*30)
    print(f"your Balance is {Balance:.2f} Le")


def Deposit ():
    Amount =float(input("Enter The Number You Want To Deposit: "))
    print("="*30)
    print("="*30)
    if Amount<0:
        print("Invalid Amount")
        return 0
    

    else:
        return Amount
    

def withdraw():
    Amount =float(input("Enter The Number You Want To Withdraw: "))

    if Amount > Balance:
        print("Not Enough")
        return 0
    

    elif Amount < 0 :
        print("Must Be Greater Than 0")
        return 0
    

    else:
      return Amount 


Balance = 0
Running = True
while Running== True:
    print("="*30)
    print("="*30)
    print("Welcome To Your Account")
    print("1- Show My Balance")
    print("2- For Deposit")
    print("3- For Withdraw")
    print("4- For Exit")
    print("="*30)
    print("="*30)
    choice =input("Please Choose Number From (1,2,3,4):")
    if choice == "1":
        Show_Balance()


    elif choice=="2":
      Balance = Balance + Deposit()


    elif choice =="3":
      Balance = Balance - withdraw()


    elif choice =="4":
        Running=False


    else:
        print("Invalid Choice")

print("="*30)
print("Thank You for Using Our Bank")
print("="*30)