import sqlite3

db = sqlite3.connect('users.db')
c = db.cursor()

# If the database does not exist, then create it
c.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT
)
""")
db.commit()

already_was=None # Variable to enter into the database

print('Registration in BD \n')

us_login = input("Enter login: ")
us_password = input("Enter password: ")

# database check cycle
for value in c.execute("SELECT * FROM users"):
    if value[0]==us_login:
        already_was='already' # If you find such a login - reset and enter that it already exists
        break

# Enter/reject
if already_was=='already':
    print('This account is already registered')
else:
    c.execute(f"INSERT INTO users VALUES (?, ?)", (us_login, us_password)) # If there was no such login, we enter it
    db.commit()
    print('Registering...')
