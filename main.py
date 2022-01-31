from ast import While
from os import remove
import this
import bank

my_bank = bank.Bank()
my_bank._load()
my_bank.add_customer("Yana Mitskevich", "19880821")
my_bank.add_customer("Roman Deputat", "19810418")
my_bank.add_account("19880821")
my_bank.add_account("19880821")
my_bank.add_account("19810418")
my_bank.add_account("19810418")
while True:
    print()
    print("Welsome to YanaBank!")
    print("Input 1 to see all customers")
    print("Input 2 to add new customer")
    print("Input 3 to get customer")
    print("Input 4 to change customer's name")
    print("Input 5 to remove customer")
    print("Input 6 to add account")
    print("Input 7 to get account")
    print("Input 8 to close account")
    print("Input 9 to put money to account")
    print("Input 10 to get money")
    print("Input # to exit app")

    x = input()
        
    if x == "1":
        customers = my_bank.get_customers()
        print("List of customers:")
        for customer in customers:
            print(customer.id, customer.name, customer.person_numer)

    elif x == "2":
        print("Enter customer's name: ")
        new_customer_name = input()
        print("Enter customer's personnumer: ")
        new_customer_pnr = input()
        my_bank.add_customer(new_customer_name, new_customer_pnr)

    elif x == "3":
        print("Enter personnumer: ")
        personnumer = input()
        customer = my_bank.get_customer(personnumer)
        if customer == None:
            print("This customer is not founded")
        else:
            print(f"Customer:  {customer.name}   {customer.person_numer}")
            for acc in customer.accounts:
                print(f"   {acc.konto_numer}   {acc.kontotyp}   {acc.saldo}")

    elif x == "4":
        print("Enter personnummer: ")
        personnumer = input()
        print("Enter new customer's name: ")
        new_name = input()
        if my_bank.change_customer_name(new_name, personnumer):
            print("New customer's name is " + new_name)
        else: 
            print("This customer is not founded")
       
    elif x == "5":
        print("Enter personnumer: ")
        personnumer = input()
        this_customer = my_bank.get_customer(personnumer)
        result = my_bank.remove_customer(personnumer)      
        if result == None:
            print("This customer is not founded")
        else:
            print("Deleted accounts are: ")
            for acc in result[0]:
                print(f"   {acc.konto_numer}   {acc.kontotyp}   {acc.saldo}")
            print(f"{this_customer.name}  got: {result[1]}")

    elif x == "6":
        print("Enter personnumer: ")
        personnumer = input()
        konto_numer = my_bank.add_account(personnumer)    
        if konto_numer == -1:
            print("This customer is not founded")
        else:
            print(f"Added new account: {konto_numer}")

    elif x == "7":
        print("Enter personnumer: ")
        personnumer = input()
        print("Enter kontonumer: ")
        account_id = int (input())
        account = my_bank.get_account(personnumer, account_id)
        if account == False:
            print("This customer is not founded")
        elif account == None:
            print("This account is not founded")
        else:
            print(f"Account:  {account.konto_numer}   {account.kontotyp}   {account.saldo}")

    elif x == "8":
        print("Enter personnumer: ")
        personnumer = input()
        print("Enter kontonumer: ")
        account_id = int(input())
        saldo = my_bank.close_account(personnumer, account_id)
        if saldo  == -1:
            print("This account is not founded")
        else:
            print(f"Account is closed. Last balance is {saldo}")
    
    elif x == "9":
        print("Enter personnumer: ")
        personnumer = input()
        print("Enter kontonumer: ")
        account_id = int(input())
        print("Enter amount for deposit: ")
        amount = float(input())
        result = my_bank.deposit(personnumer, account_id, amount)
        if result == True:
            print(f"Deposit successfully done!")
        else:
             print(f"Deposit didn't success. Please try again.")

    elif x == "10":
        print("Enter personnumer: ")
        personnumer = input()
        print("Enter kontonumer: ")
        account_id = int(input())
        print("Enter amount for withdraw: ")
        amount = float(input())
        result = my_bank.withdraw(personnumer,account_id, amount)
        if result == True:
            print(f"Withdraw successfully done!")
        else:
            print(f"Account was not found or not enough money on your account.")
       
    elif x == "#":
        break
    else:
        print("Error! Try again")
    
