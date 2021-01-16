DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS items;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL 
);

CREATE TABLE item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    price REAL NOT NULL,
    description TEXT NOT NULL,
    stock INTEGER NOT NULL
);

INSERT INTO item (name, price, description, stock) 
VALUES ("PlayStation5", 499.99, "Sony PlayStation5 with one controller", 100);

INSERT INTO item (name, price, description, stock) 
VALUES ("XBOX SeriesX", 499.99, "Microsoft XBox Series X with one controller", 100);

INSERT INTO item (name, price, description, stock) 
VALUES ("IPhone 12 Pro", 1000.50, "Apple Iphone 12 Pro with 256GB storage", 100);

INSERT INTO item (name, price, description, stock) 
VALUES ("Xperian Laptop", 780.00, "Dell Xperian 17in laptop with 16GB RAM and 1TB storage", 100);

INSERT INTO item (name, price, description, stock) 
VALUES ("IPad Pro", 1201.99, "Apple Ipad Pro with 256GB storage wifi only", 100);


