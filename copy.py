# User can:
# 	•	Create/login account
# 	•	Deposit
# 	•	Withdraw
# 	•	Check balance

# Concepts:
# 	•	List to store accounts
# 	•	Loops for menu
# 	•	Functions for operations

#list username and password / login or sign up
#UI first create acc hanyo bhani create wala function ma hit hunu paryo > asks username and password
#UN and PW should be saved in list

users_list = {
    "suvam" : "pass"
}
class Bank:
    def signup(self):
        user_name = input("Create username : ")
        if user_name in users_list:
            print ("Account exists, login instead")
            return False
        else :
            user_password = input("Create password : ")
            users_list[user_name] = user_password
            print(f"Hello !!! {user_name}")
            return True

    def login(self):
        user_name = input("Enter username : ")
        user_password = input("Enter password : ")
        if user_name not in users_list:
            print("Account not found, signup instead")
            return False
        if users_list[user_name] == user_password:
            print(f"Welcome back !!! {user_name}")
            return True
        else :
            while users_list[user_name] != user_password:
                print("Wrong password, try again")
                user_password = input("Enter password : ")
            print(f"Welcome back !!! {user_name}")
            return True

    def menu(self):
        while True:
            print("\nWelcome to the Bank")
            print("1. Login")
            print("2. Signup")
            print("3. Exit")
            choice = input("Enter choice: ")
            
            if choice == '1':
                success = self.login()
                if success:
                    bank.bank_balance()
                    break
            elif choice == '2':
                success = self.signup()
                if success:
                    bank.bank_balance()
                    break
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
            
            
    def bank_balance(self):
        initial_balance = 0
        current_balance = 100
        maximum_limit = 10000
        print(f"Current balance : {current_balance}")
        while True:
            amount = self.menu2()
            current_balance += amount
            if current_balance < maximum_limit:
                if current_balance != initial_balance:
                    print(f"Current balance : {current_balance }")
                elif(current_balance < initial_balance):
                    print("Limit exceeded")
            else:
                print("Limit exceeded")
            break
        
    
    def menu2(self):
        choice = int(input("Enter 1 to deposit \nEnter 2 to withdraw : "))
        if choice == 1:
            deposit_amount = float(input(f"Enter amount : "))
            print(f"{deposit_amount} has been added.")
            return deposit_amount
        
        elif choice == 2:   
            withdraw_amount = float(input(f"Enter amount : "))
            print(f"{withdraw_amount} has been deducted.")
            return -withdraw_amount

        else:
            print ("no")
            

bank = Bank()
bank.menu()



