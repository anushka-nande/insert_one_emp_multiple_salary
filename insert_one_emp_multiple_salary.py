import mysql.connector
from faker import Faker
import random

# ---------- DB Config ----------
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Anushka@12"
DB_NAME = "Company"
# -------------------------------

fake = Faker()

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    print("✅ Connected to MySQL successfully!\n")
except mysql.connector.Error as err:
    print("❌ Error:", err)
    exit()

# ---------- Step 1: Create 1 Employee ----------
name = input("Enter Employee Name: ➤ ")
position = input("Enter Employee Position: ➤ ")

cursor.execute(
    "INSERT INTO employee (name, position) VALUES (%s, %s)",
    (name, position)
)
emp_id = cursor.lastrowid
print(f"\n👤 Employee created: {name} | Position: {position} | ID: {emp_id}")

# ---------- Step 2: Auto-generate N Salaries ----------
n = int(input("How many salary entries to generate? ➤ "))

print(f"\n💸 Generating {n} salaries for {name}...\n")

for i in range(n):
    salary_amount = random.randint(80000, 120000)  # Example: all around ₹1 Lakh
    cursor.execute(
        "INSERT INTO salary (emp_id, amount) VALUES (%s, %s)",
        (emp_id, salary_amount)
    )
    print(f"   ✅ Salary #{i+1} = ₹{salary_amount}")

# Final commit
conn.commit()

# ---------- Step 3: Display All ----------
print(f"\n📋 All salary entries for {name}:")
cursor.execute("SELECT amount FROM salary WHERE emp_id = %s", (emp_id,))
rows = cursor.fetchall()

for idx, (amount,) in enumerate(rows, start=1):
    print(f"   {idx}. ₹{amount}")

# Close connection
conn.close()
print("\n✅ All done successfully!")
