CREATE TABLE profiles (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    education TEXT,
    work TEXT,
    github TEXT,
    linkedin TEXT,
    portfolio TEXT
);

CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    name TEXT,
    profile_id INTEGER,
    FOREIGN KEY(profile_id) REFERENCES profiles(id)
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    link TEXT,
    skill TEXT,
    profile_id INTEGER,
    FOREIGN KEY(profile_id) REFERENCES profiles(id)
);
