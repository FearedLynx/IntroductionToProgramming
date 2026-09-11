bal = 1000

def miniBank():
    global bal
    print("/" * 50)
    print("1 # Check balance")
    print("2 # Deposit money")
    print("3 # Withdraw money")
    print("4 # Exit")
    choice = int(input("Choose an option "))
    if choice == 1:
        print("Your current balance is ", bal)
        miniBank()
    elif choice == 2:
        deposit = int(input("How much money you want to deposit? "))
        bal += deposit
        print("Your current balance is ", bal)
        miniBank()
    elif choice == 3:
        withdraw = int(input("How much money you want to withdraw? "))
        if withdraw > bal:
            print("Insufficient money to withdraw ")
        else:
            bal -= withdraw
            print("Your current balance is ", bal)
        miniBank()
    elif choice == 4:
        print("Goodbye!")
        exit()
    else:
        print("Wrong input!")
        miniBank()

miniBank()
