print("*** HDFC ***")
customers = [{
    "card":12345,
    "pin":1111,
    "name":"John",
    "balance":1000
},
{
    "card":7895460,
    "pin":2222,
    "name":"Cathy",
    "balance":1000
}
]
             
print("Hello ",customers["name"])
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    ch = input("Enter your choice: ")
    if ch=="1":
        amount=int(input("Enter amount: "))
        # balance=balance+amount
        customers["balance"]= customers["balance"]+amount
        print("Your current balance is ",customers["balance"])
    elif ch=="2":
        amount=int(input("Enter amount: "))
        if amount > balance:
            print("Insufficient Balance")
        else:
            balance=balance-amount
        print("Your current balance is ",customers["balance"])
    elif ch=="3":
        break
    else:
        print("Invalid Input")
        
    