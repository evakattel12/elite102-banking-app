import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("""CREATE TABLE bank_accounts (
                id  INTEGER PRIMARY KEY AUTOINCREMENT, 
                name    TEXT NOT NULL, 
                account TEXT NOT NULL, 
                balance REAL DEFAULT 0.0)
                """)
cur.execute("""INSERT INTO bank_accounts (id, name, account, balance) VALUES
                (1, 'Marie Grace', 'Checking', 500),
                (2, 'Jose Garcia', 'Savings', 300),
                """)
con.commit()
print("Database successfully loaded!")

def account_info():
    cur.execute("SELECT name FROM bank_accounts WHERE id = ?", (id, ))


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
    choice = int(input("1. Withdrawal\n 2. Deposit"))
    if choice == 1:
        withdraw(id, amount)
    elif choice == 2:
        deposit(id, amount)

def menu():
    choice = 0
    print("Welcome to the Banking App!")
    while True:
        choice = int(input("1. Account Info \n 2. Balance \n 3. Withdrawal/Deposit \n 4. Exit "))
        if choice == 1:
            account_info()
        elif choice == 2:
            balance_display()
        elif choice == 3:
            withdepo()
        elif choice == 4:
            print("Thank you for using the Banking App!")
            cur.execute("DROP TABLE bank_accounts")
            con.commit()
            break

def main():
    init_db()
    menu()

main()
