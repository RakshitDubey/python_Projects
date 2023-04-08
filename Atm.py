import sys
class Atm:


    def __init__(self):
        self.pin=1234
        self.balance=50000



    def menu(self):
        print("""
        Select Options:
        1.Check Balance
        2.withdraw balance
        3.Deposit balance
        4.Exit
        """)

        options=int(input("Enter Your option:"))
        if options==1:
            self.checkbalance()
           
        elif options==2:
            self.withdraw()

        elif options==3:
            self.deposit()

        elif options==4:
            sys.exit()

    
    def checkbalance(self):
        input_pin=int(input("Enter Your pin"))
        if input_pin==self.pin:
            print(f'your Balance is{self.balance}')

        else:
            print("Your pin is incorrect")

        self.menu()
            

    def withdraw(self):
        input_pin=int(input("Enter Your pin"))
        if input_pin==self.pin:
            draw=int(input("Enter your withdraw amount"))

            if draw<=self.balance:
                self.balance=self.balance-draw
                print("Now Your balance is",self.balance)

            else:
                print('insufficient balance')
        else:
            print("Your pin is incorrect")

        self.menu()

    

    def deposit(self):
        input_pin=int(input("Enter Your pin"))
        if input_pin==self.pin:
            deposit=int(input("Enter deposit amount"))
            self.balance=self.balance+deposit

        else:
            print("check pin")
        
        self.menu()



sbi=Atm()
sbi.menu()