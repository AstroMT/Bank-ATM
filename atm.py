class atm(object):
    def __init__(self, cardNumber, cardPin, balance, expirationDate):
        self.cardNumber = cardNumber
        self.cardPin = cardPin
        self.balance = balance
        self.expirationDate = expirationDate

    def buyProduct(cost, tax):
        totalcost = user_info.balance - cost - tax*cost
        if totalcost > user_info.balance:
            print("Not enough money to buy the product")
            main()
        elif user_info.expirationDate < 2023:
            print("Your card has expired")
        else:
            print("There is enough money to buy the product")
            main()

    def checkBalance():
        print(user_info.balance)
        main()

    def withdraw(amount):
        if amount > user_info.balance:
            print("You cannot withdraw this much")
            main()
        elif user_info.expirationDate < 2023:
            print("Your card has expired")
        else:
            print("You can withdraw this much")
            main()
    

def get_inputs():
    user_cn = input("Enter your card number (16 digits): ")
    try:
        user_cn = int(user_cn)
    except:
        print("Card number must be a 16-digit number")
    
    user_cp = input("Enter your card pin (4 digits): ")
    try:
        user_cp = int(user_cp)
    except:
        print("Card pin must be a 4-digit number")
    
    user_bal = input("Enter your balance: ")
    try:
        user_bal = int(user_bal)
    except: 
        print("Invalid balance")
    
    user_expdt = input("Enter the year of the card's expiration date: ")
    try:
        user_expdt = int(user_expdt)
    except: 
        print("Invalid expiration date")
        
    return user_cn, user_cp, user_bal, user_expdt


def main():
    activity = input("What do you want to do? Enter BP (buy product), CB (check balance), or WC (withdraw cash)? ")
    if activity == 'BP':
        cost = input("Enter the cost of the item: ")
        try:
            cost = float(cost)
        except:
            print("Must be a number")
        
        tax = input("Enter the tax percentage (0-100)")
        try:
            tax = float(tax)
        except:
            print("Must be a number")

        if tax > 0 and tax < 100:
            atm.buyProduct(cost, tax)
        else:
            print("Tax out of range")

    elif activity == "CB":
        atm.checkBalance()

    elif activity == 'WC':
        amount = input("How much money would you like to withdraw? ")
        try:
            amount = float(amount)
        except:
            print("Not a number")

        atm.withdraw(amount)

user_cn, user_cp, user_bal, user_expdt = get_inputs()
user_info = atm(user_cn, user_cp, user_bal, user_expdt)

main()