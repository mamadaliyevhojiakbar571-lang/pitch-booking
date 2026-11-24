CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS pitches(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    price INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY(owner_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS bookings(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    pitch_id INTEGER NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES users(id),
    FOREIGN KEY(pitch_id) REFERENCES pitches(id)
);


