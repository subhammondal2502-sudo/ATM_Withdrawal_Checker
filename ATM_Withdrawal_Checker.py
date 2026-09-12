#ATM Withdrawal Checker..........
balance=float(input("enter your balance : "))
withdraw_amount=float(input("enter your withdraw_amount : "))
Remaining_balance=balance-withdraw_amount
print("balance : ", balance)
print("withdraw_amount : ", withdraw_amount)
if balance < 0:
    print("Invalid balance")
