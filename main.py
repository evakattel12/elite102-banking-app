import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

# Delete the tables from the previous run of the program.
cur.execute("DROP TABLE IF EXISTS bank_accounts")
cur.execute("DROP TABLE IF EXISTS transactions")
con.commit()

# Create the two tables bank_accounts and transactions. bank_accounts currently works (as seen in tutorial.db).
cur.execute("""CREATE TABLE IF NOT EXISTS bank_accounts (
                id  INTEGER PRIMARY KEY AUTOINCREMENT, 
                name    TEXT NOT NULL, 
                account TEXT, 
                balance REAL DEFAULT 0.0)
                """)
con.commit()
print("Database successfully loaded!\nTables loaded: Bank Accounts\n")

# Main menu function here. This is the CLI interface the user interacts with to access the banking app.
def menu():
    choice = 0
    print("Welcome to the Claridea Banking App!")
    name = input("Please enter your name: ")
    while True:
        choice = int(input(" 1. Accounts \n 2. Withdraw \n 3. Deposit \n 4. Exit \n"))
        if choice == 1:
            ask = int(input("1. Create Accounts \n2. View Accounts \n"))
            accounts(name, ask)
        elif choice == 2:
            take_out = float(input("How much would you like to take out from your account?\n"))
            withdraw(name, take_out)
        elif choice == 3:
            put_in = float(input("How much would you like to put into your account?\n"))
            deposit(name, put_in)
        elif choice == 4:
            print("Thank you for using the Claridea Banking App!")
            break

# Accounts function where the name of the user is used like an ID to find them in the table bank_accounts. Their choice from the menu dictates which path the function goes through.
def accounts(name, choice):
    if choice == 1:
        init_depo = float(input("How much do you want your initial balance to be?\n"))
        while init_depo <= 0:
            init_depo = float(input("Please try again. How much do you want your initial balance to be?\n"))
        acct_type = input("Are you creating a savings or a checking account? (Only enter ""Checking"" or ""Saving"")\n")
        create_accounts(name, init_depo, acct_type)
    elif choice == 2:
        view_accounts(name)

# Accounts function where the name of the user is used like an ID to find them in the table bank_accounts. Their choice from the menu dictates which path the function goes through.
def create_accounts(name, initial = 0.0, type = "savings"):
    cur.execute("INSERT INTO bank_accounts (name, balance, account) VALUES (?, ?, ?)", (name, initial, type))
    con.commit()
    print(f"Account has been created for {name} with a balance of ${initial:.2f}")
    print("")

# Function where the user can view all of their accounts in the app.
def view_accounts(name):
    cur.execute(f"SELECT * FROM bank_accounts WHERE name = '{name}'")
    for row in cur.fetchall():
        print(row)
        print("")

# Withdrawal function where the user can take money out of their account.
def withdraw(name, take_out):
    print("Function accessed: withdraw")
    if take_out <= 0:
        print("Error: Deposit must be positive.")
        return
    balance = balance_check(name)
    if take_out > balance:
        print(f"Error: Insufficient funds. Balance: ${balance:.2f}, Requested: ${take_out:.2f}")
        return
    cur.execute("UPDATE bank_accounts SET balance = balance - ? WHERE name = ?", (take_out, name))
    con.commit()
    new_balance = balance_check(name)
    print(f"Withdrew ${take_out:.2f}. New Balance: ${new_balance:.2f}")

# Deposit function where the user can deposit money into their account.
def deposit(name, put_in):
    if put_in <= 0:
        print("Error: Deposit must be positive.")
        return
    cur.execute("UPDATE bank_accounts SET balance = balance + ? WHERE name = ?", (put_in, name))
    con.commit()
    balance = balance_check(name)
    print(f"Deposit Amount: ${put_in}. New balance: ${balance:.2f}")

# Balance checking function where the account balance under the person's name is checked.
def balance_check(name):
    cur.execute("SELECT balance FROM bank_accounts WHERE name = ?", (name,))
    row = cur.fetchone()
    if row is None:
        print(f"Error: No accounts under name '{name}'")
        return 0.0
    return row[0]

# Main function where the whole program runs.
def main():
    menu()

main()