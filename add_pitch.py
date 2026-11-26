import sqlite3
connection = sqlite3.connect("pitch_booking.db")
connection.execute("PRAGMA foreign_keys = ON")

name = "Bunyodkor"
location = "Sergeli metro"
price = 150000
owner_id = 2

try:
    connection.execute(
        "INSERT INTO pitches(name, location, price, owner_id) VALUES(?, ?, ?, ?)", (name, location, price, owner_id)
    )
    connection.commit()
    print("Muvaffaqiyatli qo'shildi")
except sqlite3.IntegrityError as e:
    error_msg = str(e)
    if "NOT NULL constraint failed" in error_msg:
        column_name = error_msg.split(".")[-1]
        print(f"Iltimos, {column_name} maydonini to'ldiring")
    elif "FOREIGN KEY constraint failed" in error_msg:
        print(f"Xatolik: ID={owner_id} bo'lgan foydalanuvchi bazada mavjud emas!")
    else:
        print(f"Ma'lumotlar bazasida kutilmagan xatolik yuz berdi: {e}")
finally:
    connection.close()