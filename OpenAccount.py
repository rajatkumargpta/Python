# csb Bank 
print (" enter your age . ")
age = int(input())
if (age<18):
    print("you can open minor account ")
else:
    print("you can open account")
    print("Please Select Account Type : ")
    print("1. Savings Account")
    print("2. Current Account")
    print("3. NRI Account")
    account_type = int(input())
    if(account_type==1):
        print("Opening Savings Account")
    elif(account_type==2):
        print("Opening Current Account")
    else:
        print("Invalid Account Type!")

SomeError