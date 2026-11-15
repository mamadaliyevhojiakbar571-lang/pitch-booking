# ⚽ Pitch Booking

## Nima qiladi?

Futbol maydonlarini bron qilish tizimi. O'yinchilar maydonlardagi bo'sh vaqtni bron qiladi, maydon egalari esa o'z maydonlari va vaqtlarini boshqaradi.

Tizim asosan birga futbol o'ynaydigan mahalliy guruhlar va do'stlar uchun mo'ljallangan, lekin futbol o'ynashni istagan har kim bron qila oladi.

## Rollar

- **owner** (maydon egasi):
  - yangi maydon qo'shadi
  - maydon narxini o'zgartiradi
  - maydon vaqtlarini o'zgartiradi
- **customer** (o'yinchi):
  - o'ziga qulay maydonni tanlaydi: narxi va manzilini ko'radi
  - bo'sh vaqtni bron qiladi
  - bronni bekor qiladi
  - maydon egasining telefon raqamini oladi

## Jadvallar

- `foydalanuvchilar`: id, ism, email, parol, rol, telefon
- `maydonlar`: id, nomi, manzil, narxi, ega_id
- `bronlar`: id, mijoz_id, maydon_id, boshlanish, tugash, holat

---

## 🇬🇧 What does it do?

A booking system for football pitches. Players book free time slots on pitches,
while pitch owners manage their pitches and schedules.

It is mainly designed for local groups and friends who play football together,
but anyone who wants to play can make a booking.

## Roles

- **owner** (pitch owner):
  - adds new pitches
  - changes pitch prices
  - changes pitch schedules
- **customer** (player):
  - chooses a convenient pitch: sees its price and location
  - books a free time slot
  - cancels a booking
  - gets the pitch owner's phone number

## Tables

- `users`: id, name, email, password, role, phone
- `pitches`: id, name, location, price, owner_id
- `bookings`: id, customer_id, pitch_id, start_time, end_time, status
