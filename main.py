from User import *
from Admin import *
def main():
    current_user  = None
    Admin_user  = None
    while True:
        if current_user == None and Admin_user == None:
            print("-|Press 1 to Create an account")
            print("-|Press 2 to login in  your account")
            print("-|Press 3 to Admin Login")
            print("-|Press 4 Exit")
            x = int(input("Enter your option : "))
            if x == 1 :
                print()
                print("Which type of account do you want to make?")
                print("-|Press 1 Savings")
                print("-|Press 2 Current")
                y = int(input("Enter your option : "))
                if y == 1:
                    username = (input("Enter your username : "))
                    usermail = input("Enter your mail : ")
                    userAddress = input("Enter your Address : ")
                    userpass = input("Enter your userpassword : ")
                    current_user = Savings_account(username,usermail,userAddress,userpass)
                    print(f"\n ---|  Your account Number is : {current_user.acount_numbers}   |---  \n")

                elif y == 2:
                    username = (input("Enter your username : "))
                    usermail = input("Enter your mail : ")
                    userAddress = input("Enter your Address : ")
                    userpass = input("Enter your userpassword : ")
                    current_user = Current_Acount(username,usermail,userAddress,userpass)
                    print(f"\n ---|  Your account Number is : {current_user.acount_numbers}  |---  \n")

                    
                else:
                    main()
            elif x == 2:
                username = input("Enter your username : ")
                userpass = input("Enter your userpassword : ")
                for account in User.acounts:
                    if account.name == username and account.password == userpass:
                        current_user = account
                        break
                else:
                    print("Invalid UserName Or password")
                    print("---- Try again!! ----")
            elif x == 3:
                if Admin_user == None:
                    print("-|Press 1 to create account?")
                    print("-|Press 2 to Logged in ?")
                    k = int(input("Enter your option : "))
                    if k == 1:
                        user = input("Enter your username : ")
                        pswrd = input("Enter your password : ")
                        Admin_user = Admin(user,pswrd)
                    elif k == 2:
                        user = input("Enter your username : ")
                        pswrd = input("Enter your password : ")
                        for account in Admin.admin_acounts:
                            if account.name == user and account.password == pswrd: 
                                Admin_user = account
                                break
                            else:
                                print("\n #### Invalid username or password #### \n")
                

            elif x == 4:
                break
        elif (current_user is not None):
            print(f"----- Welcome {current_user.name} --------")
            if current_user.account_type == "savings":
                  print("-| Press 1 to Show info ")
                  print("-| Press 2 to Withdraw money ")
                  print("-| Press 3 to Deposite money ")
                  print("-| Press 4 to Take Loans ")
                  print("-| Press 5 Change Info ")
                  print("-| Press 6 Check Balance ")
                  print("-| Press 7 Apply Interest ")
                  print("-| Press 8 Transection History ")
                  print("-| Press 9 Transfer Balance ")
                  print("-| Press 10 Log Out ")
                  x = int(input("Enter Your Option - "))
                  if x == 1:
                      current_user.showInfo()
                  elif x == 2:
                      amount = int(input("Enter your amount : "))
                      current_user.withdraw(amount)
                  elif x == 3:
                      amount = int(input("Enter your amount : "))
                      current_user.deposite(amount)
                  elif x == 4:
                      amount = int(input("Enter your amount : "))
                      current_user.Loan(amount)
                  elif x == 5:
                      type = input("Which information do you want to change (Name or password): ")
                      current_user.changeInfo(type)
                  elif x == 6:
                      current_user.chech_balance()
                  elif x == 7:
                      current_user.apply_interest()
                  elif x == 8:
                      current_user.Transection()
                  elif x == 9:
                      acount = input("Enter account name where to transfer : ")
                      money = int(input("Enter amount : "))
                      current_user.transfer_money(acount,money)
                  elif x == 10 :
                      current_user = None
                      main()
            elif current_user.account_type == "Current":
                  print("-| Press 1 to Show info ")
                  print("-| Press 2 to Withdraw money ")
                  print("-| Press 3 to Deposite money ")
                  print("-| Press 4 to Take Loans ")
                  print("-| Press 5 Change Info ")
                  print("-| Press 6 Check Balance ")
                  print("-| Press 7 Transection History ")
                  print("-| Press 8 Transfer Money ")
                  print("-| Press 9 Log Out ")
                  x = int(input("Enter Your Option - "))
                  if x == 1:
                      current_user.showInfo()
                  elif x == 2:
                      amount = int(input("Enter your amount : "))
                      current_user.withdraw(amount)
                      print(f"\n --- {amount} has been withdraw ---\n ")
                  elif x == 3:
                      amount = int(input("Enter your amount : "))
                      current_user.deposite(amount)
                      print(f"\n --- {amount} has been deposite ---\n ")
                  elif x == 4:
                      amount = int(input("Enter your amount : "))
                      current_user.Loan(amount)
                  elif x == 5:
                      type = input("Which information do you want to change (Name or password): ")
                      current_user.changeInfo(type)
                  elif x == 6:
                      current_user.chech_balance()
                  elif x == 7:
                      current_user.Transection()
                  elif x == 8:
                      acount = input("Enter account name where to transfer : ")
                      money = int(input("Enter amount : "))
                      current_user.transfer_money(acount,money)
                  elif x == 9 :
                      current_user = None
                      main()

        elif Admin_user is not None:
                    print(f"\n------ Welcome {Admin_user.name} -----\n")
                    print("-| Press 1 Create account")
                    print("-| Press 2 Delete account")
                    print("-| Press 3 All acount list")
                    print("-| Press 4 Total Balance")
                    print("-| Press 5 Total Loan")
                    print("-| Press 6 Loan OFF or ON ")
                    print("-| Press 7 Log Out ")
                    z = int(input("Enter your option : "))
                    if z == 1:
                        print()
                        print("Which type of account do you want to make?")
                        print("-|Press 1 Savings")
                        print("-|Press 2 Current")
                        y = int(input("Enter your option : "))
                        if y == 1:
                            username = (input("Enter your username : "))
                            usermail = input("Enter your mail : ")
                            userAddress = input("Enter your Address : ")
                            userpass = input("Enter your userpassword : ")
                            current_user = Savings_account(username,usermail,userAddress,userpass)
                            print(f"\n ---|  Your account Number is : {current_user.acount_numbers}   |---  \n")

                        elif y == 2:
                            username = (input("Enter your username : "))
                            usermail = input("Enter your mail : ")
                            userAddress = input("Enter your Address : ")
                            userpass = input("Enter your userpassword : ")
                            current_user = Current_Acount(username,usermail,userAddress,userpass)
                            print(f"\n ---|  Your account Number is : {current_user.acount_numbers}  |---  \n")

                    elif z == 2:
                        delete_acount = input("Enter delete account name : ")
                        del User.account_number[delete_acount]
                    elif z == 3:
                        for acount in User.acounts:
                            print(f"Account name - {acount.name} , Account password - {acount.password} ")
                    elif z == 4:
                        print(f"Total Available Balance of Bank {User.total_balance} ")
                    elif z == 5:
                        print(f"Total Loan amount {User.total_loans} ")
                    elif z == 6:
                        l = input("Loan system ON/OFF :")
                        if l == "ON":
                            User.isLoan = False
                        else:
                            User.isLoan = True
                    elif z == 7:
                        main()


if __name__ == '__main__':
    main()