from pickle import TRUE
import account
import customer

class Bank():
    customers = []

    last_customer_id = 111110

    def _load(self):
        file = open("data.txt", "r")
        for line in file:
            accounts = line.split("#") 
            customer = accounts[0].split(":")
            customer_id = int(customer[0])
            customer_name = customer[1]
            customer_pnr = customer[2]
            self.add_customer(customer_name, customer_pnr, customer_id)
            account_number = int(customer[3])
            account_saldo = float(customer[5])
            self.add_account(customer_pnr, account_number, account_saldo)
            for x in range (1, len(accounts)):
                account = accounts[x].split(":")
                account_number = int(account[0])
                account_saldo = float(account[2])
                self.add_account(customer_pnr, account_number, account_saldo)       
        file.close()
      

    def get_customers(self):
        return self.customers
        

    def add_customer(self, name, pnr, id=0):
        if self.get_customer(pnr) == None:
            if id > 0:
                self.last_customer_id = id
            else:
                self.last_customer_id = self.last_customer_id + 1
            new_customer = customer.Customer(self.last_customer_id, name, pnr)
            self.customers.append(new_customer)
            return True
        else:
            return False


    def get_customer(self, pnr):
        for customer in self.customers:
            if pnr == customer.person_numer:
               return customer
        return None


    def change_customer_name(self, name, pnr):
        customer = self.get_customer(pnr)
        if customer == None:
            return False
        else:
            customer.name = name
            return True


    def remove_customer(self, pnr):
        customer = self.get_customer(pnr)
        if customer == None:
            return None
        summa = 0
        for acc in customer.accounts:
            summa = summa + acc.saldo       
        self.customers.remove(customer)
        return (customer.accounts, summa) 


    def add_account(self, pnr, konto_numer = 0, saldo = 0):
        customer = self.get_customer(pnr)
        if customer == None:
            return -1

        if konto_numer == 0:
            self.last_konto_numer = self.last_konto_numer + 1
        else:
            self.last_konto_numer = konto_numer
        new_account = account.Account(self.last_konto_numer, saldo)
        customer.accounts.append(new_account)
        return new_account.konto_numer


    def get_account(self, pnr, account_id):
        customer = self.get_customer(pnr)
        if customer == None:
            return False
        for account in customer.accounts:
            if account_id == account.konto_numer:
                return account
        return None
           

    def deposit(self, pnr, account_id, amount):
        account = self.get_account(pnr, account_id)
        if account == None or account == False:
            return False
        account.saldo = account.saldo + amount
        return True
        

    def withdraw(self, pnr, account_id, amount):
        account = self.get_account(pnr, account_id)
        if account == None or account == False:
            return False
        if account.saldo < amount:
            return False
        account.saldo = account.saldo - amount
        return True
        

    def close_account(self, pnr, account_id):
        customer = self.get_customer(pnr)
        account = self.get_account(pnr, account_id)
        if account == None or account == False:
            return -1
        customer.accounts.remove(account)
        return account.saldo

        
    