import json
import os

class Bank:
    accounts={}
    transactions={}
    
    def load_data():
        """Load account and transaction data from a JSON file."""
        if os.path.exists("bank_data.json"):
            with open("bank_data.json", "r") as file:
                data = json.load(file)
                Bank.accounts = data.get("accounts", {})
                Bank.transactions = data.get("transactions", {})
                
    def save_data():
        """Save account and transaction data to a JSON file."""
        with open("bank_data.json", "w") as file:
            data = {
                "accounts": Bank.accounts,
                "transactions": Bank.transactions
            }
            json.dump(data, file, indent=4)
    
    
    
    
    
    def __init__(self,ac_no,ac_name,password,bal=0):
        self.ac_no=ac_no
        self.bal=bal
        self.ac_name=ac_name
        self.password=password
        Bank.accounts[ac_no]=self
        Bank.transactions[ac_no]=[]
        Bank.save_data()
        
    def create_account():
        ac_no=int(input("enter ac number "))
        ac_name=input("enter ac holder name")
        bal=int(input("enter initial amount to deposit"))
        password=input("enter ac password")
        if ac_no  in Bank.accounts:
            print("ac number already exists try again with different number")
            return
        Bank(ac_no,ac_name,password,bal)
        
    def deposit():
        ac_no=int(input("enter ac number to deposit money"))
        if ac_no not in Bank.accounts:
            return
        amount=int(input("enter amount to deposit"))
        if amount>=0:
            Bank.accounts[ac_no].bal+=amount
            Bank.transactions[ac_no].append(amount)
            print("successfully deposited , total money=",Bank.accounts[ac_no].bal)
            Bank.save_data()
        else:
            print("amount should be greater than or equal to 1 ")
    def withdraw():
        ac_no=int(input("enter ac number to deposit money"))
        amount=int(input("enter amount to withdraw"))
        if Bank.accounts[ac_no].bal>=amount:
            Bank.accounts[ac_no].bal-=amount
            Bank.transactions[ac_no].append(amount)
            print("successfully debited , total money=",Bank.accounts[ac_no].bal)
            Bank.save_data()
        else:
            print("you have insufficient balance=",Bank.accounts[ac_no].bal)
    def viewtransactions():
        ac_no=int(input("enter ac number to view your transactions"))
        if ac_no not in Bank.accounts:
            return
        for i in Bank.transactions[ac_no]:
            print(i)

    def transfer():
        ac_no=int(input("enter your ac number to transfer from your account : "))
        amount=int(input("enter amount to transfer : "))
        if ac_no not in Bank.accounts:
            print("your ac is not exists")
            return
        if amount>Bank.accounts[ac_no].bal:
            print("your account blance is not enough ")
            return
        reciept_ac  =int(input("enter your ac number of reciever : "))
        if reciept_ac not in Bank.accounts:
            print("recieptant not exists")
            return
        password = input("enter your account password")
        if password == Bank.accounts[ac_no].password:
            Bank.accounts[ac_no].bal-=amount
            Bank.accounts[reciept_ac].bal+=amount
        else:
            print("password wrong")
            return
    def view_ac():
        ac_no=int(input("enter your ac number to view your details: "))
        password = input("enter your account password")
        if password == Bank.accounts[ac_no].password:
            print("Name : ",Bank.accounts[ac_no].ac_name)
            print("ac no : ",Bank.accounts[ac_no].ac_no)
            print("Balance : ",Bank.accounts[ac_no].bal)
            
        
Bank.load_data()
while True:
    print("Welcome to bank ")
    print("1.create account")
    print("2.deposit")
    print("3.withdraw")
    print("4.View tansanctions")
    print("5.Transfer money to other account")
    print("6View your ac details")
    print("7.exit")
    choice=int(input("Choose your option : "))
    if choice==1:
        Bank.create_account()
    elif choice==2:
        Bank.deposit()
    elif choice==3:
        Bank.withdraw()
    elif choice==4:
        Bank.viewtransactions()
    elif choice==5:
        Bank.transfer()
    elif choice==6:
        Bank.view_ac()
    elif choice==7:
        exit()
    else:
        print("you entered an invalid input try again")