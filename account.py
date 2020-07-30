def show_withdrawals_statement(self):
        for  withdrawal in self.withdrawals:
                time = withdrawals["time]
                formatted_time = self.pet_formatted_time(time)
                amount = withdrawal["amount"]
                statement = "You withdraw {} on {}". format (amount, formatted_time)
                print(withdrawal)def request_loan(self, amount):
       try:
             amount + 10
      except TypeError:
               print("Please enter the requested amount in figures")
              return 
if amount <= 0:
       print(You cannot request a loan of that amount")
else: 
       self.loan = amount 
       print("You have been given  a loan of {}". format(amount))
def repay_loan(self, amount):
       try:
            amount + 10
      except TypeError:
               print("Enter the repayment in figures")
               return
if amount <= 0:
       print ("You cannot repay with that  amount")
elif self.loan == 0:
      print("You  don't have  a loan at the moment")
elif amount > self.loan:
      print("Your loan  is {}, please enter an amount that is less or equal".format(self.loan))
else:
       self.loan -= amount
       time = datetime.now()
        repayment = {
                "time": time,
                " amount": amount
}
        self.loan_repayments.append(repayment)
print("You have repaid your loan with {}. Your loan balance is {}". format(amount, self.loan))
def loan_repayment_statement(self):
         for repayment in self.loan_repayments:
                 time = repayment["time"]
                 amount = repayment["amount"]
                 formatted_time = self.get_formatted_time(time)
                 statement = "You repaid  {} on {}". format(amount, formatted_time)
                print (statement)
    Class BankAccount {Account}:
         def _init_(self, first_name, last_name, phone_number):
               self.bank = bank
               super()._init _ (first_name, last_name, phone_number)
classMobileMoney Account(Account):
        def _init_(self, first_name, last_name, phone_number, service_provider):
               self.service_provider = service_provider
self.airtime = []
super()._init_(first_name, last_name, phone_number)
        def buy_airtime(self, account):
try:
      amount + 1
except  TypeError:
         print("please enter the amount in figures")
         return
if amount > self.balance:
       print("You don't have enough balance, your balance is {}".format(self.balance)
else: 
       self.balance -= amount 
       time = datetime.now()
airtime ={
        "time": time,
        "airtime": amount
}
self.airtime.append(airtime)
print{"You have bought airtime worth{} on {}".format(amount, self.get_formatted_time(time)))
