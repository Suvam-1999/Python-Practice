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
    "suvam" : "1234"
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
                success = bank.login()
                if success:
                    break
            elif choice == '2':
                success = bank.signup()
                if success:
                    break
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
            
            

bank = Bank()
bank.menu()


