import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE bank_accounts(id, name, account, balance)")
cur.execute("""INSERT INTO bank_accounts VALUES
            (1, 'Marie Grace', 'Checking', 500),
            (2, 'Jose Garcia', 'Savings', 300)
            """)
con.commit()