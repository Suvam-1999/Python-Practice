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


class User:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def email(self):
        print("email")
    def balance(self):
        print("balance")

suvam = User(10, 30)
print (suvam.y, suvam.x)






