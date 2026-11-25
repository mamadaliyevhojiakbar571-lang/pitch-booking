import sqlite3

connection = sqlite3.connect("pitch_booking.db")
connection.execute("PRAGMA foreign_keys = ON")

name = "Ali"
email = "ali@example.com"
password = "12345678"
role = "customer"
phone = "+998933332211"

try:
    connection.execute(
        "INSERT INTO users(name, email, password, role, phone) VALUES(?, ?, ?, ?, ?)",
        (name, email, password, role, phone)
    )
    connection.commit()
    print("Muvaffaqiyatli qo'shildi")

except sqlite3.IntegrityError as e:
    error_msg = str(e)

    if "UNIQUE constraint failed: users.phone" in error_msg:
        print(f"{phone} — bu telefon raqam allaqachon ro'yxatdan o'tgan")
    elif "UNIQUE constraint failed: users.email" in error_msg:
        print(f"{email} — bu email allaqachon ro'yxatdan o'tgan")
    elif "NOT NULL constraint failed" in error_msg:
        column_name = error_msg.split(".")[-1]
        print(f"Iltimos, '{column_name}' maydonini to'ldiring")
    else:
        print("Baza xatoligi:", error_msg)

finally:
    connection.close()
