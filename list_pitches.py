import sqlite3

connection = sqlite3.connect("pitch_booking.db")

try:
    print("\nMaydonlarni narxi bo'yicha saralash:")
    print("1 - Eng qimmatidan (kattasidan kichigiga)")
    print("2 - Eng arzonidan (kichigidan kattasiga)")

    selection = input("Tanlovingizni kiriting (1 yoki 2): ").strip()

    if selection == "1":
        order = "DESC"
    elif selection == "2":
        order = "ASC"
    else:
        print(
            "\nNoto'g'ri tanlov! Faqat 1 yoki 2 raqamini kiriting. Hozircha eng"
            " arzonidan ko'rsatilmoqda."
        )
        order = "ASC"

    cursor = connection.execute(
        f"""
        SELECT pitches.name, pitches.location, pitches.price, users.name, users.phone 
        FROM pitches
        JOIN users ON pitches.owner_id = users.id
        ORDER BY pitches.price {order}
        """
    )

    results = cursor.fetchall()

    if results:
        for pitches_name, location, price, users_name, users_phone in results:
            print(f"🏟  {pitches_name}")
            print(f"📍 Manzil: {location}")
            print(f"💰 Narxi:  {price:,} so'm / soat")
            print(f"👤 Egasi:  {users_name}")
            print(f"📞 Tel:    {users_phone}")
            print("-" * 35)
    else:
        print("Bazada maydonlar mavjud emas!")

except sqlite3.Error as error:
    print("Xato:", error)
finally:
    connection.close()
