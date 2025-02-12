# Create Account class with 2 attributes - balance & account no.
# # Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, account_no, balance= 0):
        self.account_no= account_no
        self.balance= balance
    
    def credit(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"Your account has been credited to {amount}, your new balance is {self.balance}")
        else:
            print("Insufficient Credit Balance")

    def debit(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Your account has been debited to {amount} your new balance is {self.balance}")
        else:
            print("You have to recharge")
    
    def print_balance(self):
        print(f"Your manin balance is {self.balance}")

user_account= int(input("Enter your Account Number: "))
# user_amount= int(input("Enter your Amount: "))
main_account= Account(user_account, 10000)
main_account.print_balance()
transaction_type= input("Do you want to Credit/Debit? ").strip().lower()
if transaction_type =="credit":
    user_credit= int(input("Enter your Credit amount:  "))
    main_account.credit(user_credit)
elif transaction_type =="debit":
    user_debit= int(input("Enter your Debit amount:  "))
    main_account.debit(user_debit)
else:
    print("Invalid Decission")
main_account.print_balance()


# Note: The .strip() method is used to remove any leading or trailing whitespace from the user's input. This ensures that if the user accidentally enters a space before or after their choice (e.g., " credit " instead of "credit"), the program will still recognize the input correctly.
# If the user inputs " credit ", .strip() will convert it to "credit", preventing unnecessary errors.
# .lower() further ensures that variations like "Credit" or "CREDIT" are properly interpreted as "credit".