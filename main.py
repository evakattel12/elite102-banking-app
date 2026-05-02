import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
# Create the two tables bank_accounts and transactions. bank_accounts currently works (as seen in tutorial.db), but transactions has issues.
cur.execute("""CREATE TABLE bank_accounts (
                id  INTEGER PRIMARY KEY AUTOINCREMENT, 
                name    TEXT NOT NULL, 
                account TEXT, 
                balance REAL DEFAULT 0.0)
                """)
cur.execute("""CREATE TABLE transactions (
                id  INTEGER PRIMARY KEY AUTOINCREMENT, 
                acct_id    INTEGER,
                timestamps DATETIME DEFAULT CURRENT_TIMESTAMP, 
                amount REAL
                type TEXT)
                """)
#cur.execute(INSERT INTO bank_accounts (id, name, account, balance)
#                (1, 'Marie Grace', 'Checking', 500.0),
#                (2, 'Jose Garcia', 'Savings', 300.0),
#                """)
con.commit()
print("Database successfully loaded!\nTables loaded: Bank Accounts, Transactions\n")

def account_info(name, init_deposit):
    while True:
        ask = input("Do you currently have an account here? (Y/N)")
        if ask.lower() == "y":
            cur.execute("SELECT name FROM bank_accounts WHERE id = ?", (id, ))
        if ask.lower() == "n":
            cur.execute("INSERT INTO bank_accounts (name, balance) VALUES (?, ?), (name, init_deposit)")
            con.commit()
            acct_id = cur.lastrowid
            if init_deposit > 0:
                cur.execute("""INSERT INTO transactions (acct_id, type, amount) VALUES (?, "Deposit", ?)""", (acct_id, init_deposit))
                con.commit()
                print(f"Account has been created for {name} (ID: {acct_id}) with a balance of ${init_deposit:.2f}")
                return acct_id

def balance_display():
    cur.execute("SELECT account, balance FROM bank_accounts where id = ?", (id, ))

def withdraw(id, amount):
    if amount <= 0:
        print("Error: Withdrawal amount cannot be negative or zero.")
        return

def deposit(id, amount):
    if amount <= 0:
        print("Error: Withdrawal amount cannot be negative or zero.")
        return

def withdepo():
    amount = int(input("How much would you like to deal with today? "))
    choice = int(input(" 1. Withdrawal\n 2. Deposit"))
    if choice == 1:
        withdraw(id, amount)
    elif choice == 2:
        deposit(id, amount)

def menu():
    choice = 0
    print("Welcome to the Banking App!")
    name = input("Please enter your name: ")
    while True:
        choice = int(input(" 1. Account Info \n 2. Balance \n 3. Withdrawal/Deposit \n 4. Exit "))
        if choice == 1:
            init_deposit = float(input("If you have a withdrawal or deposit to make, please enter it here: "))
            account_info(name, init_deposit)
        elif choice == 2:
            balance_display()
        elif choice == 3:
            withdepo()
        elif choice == 4:
            print("Thank you for using the Banking App!")
            break

def main():
    menu()

main()
