CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE pitches(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    price INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY(owner_id) REFERENCES users(id)
);

