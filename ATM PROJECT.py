import time 
print("please insert your card")
time.sleep
password=1234
pin=int(input("enter your ATM pin"))
balance = 10000
if pin==password:
    while True:
        print("""
            1 == balance
            2 == withdrawal balance
            3 == deposit balance
            4 == exit
            """)
        try:
            option = int(input("please enter your choice"))
        except:
            print("please enter valid option")
        if option==1:   
            print(balance)
        if option==2:
            withdraw_amount=int(input("please enter withdraw amount"))
            balance=balance-withdraw_amount
            print("amount is debited from your account")
            print(balance)
        if option==3:
            deposite_amount=int(input("enter the deposite amount"))
            deposite_amount=balance+deposite_amount
            print("THE CURRENT BALANCE IS ",(deposite_amount))
        if option==4:
            break
else:
    print("WORNG PIN PLEASE TRY AGAIN !!")

    1