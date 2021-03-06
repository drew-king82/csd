Drop user if exists "whatabook"@"localhost";

CREATE USER "whatabook"@"localhost" IDENTIFIED WITH mysql_native_password BY "MySQL8isgreat!";

GRANT ALL PRIVILEGES ON what_a_book.* TO "whatabook"@"localhost";

Drop table if exists Wishlist;
Drop table if exists Books;
Drop table if exists Stores;
Drop table if exists UserAccount;

CREATE TABLE UserAccount(
	user_id  INT  NOT NULL  AUTO_INCREMENT,  
	first_name  VARCHAR(75)  NOT NULL,
	last_name  VARCHAR(75)  NOT NULL,
	email_address  VARCHAR(75)  NOT NULL,
	PRIMARY KEY (user_id)
);


CREATE TABLE Books(
	book_id  INT  NOT NULL  AUTO_INCREMENT,
	book_name  VARCHAR(200)  NOT NULL, 
	details_V  VARCHAR(500),
	author  	VARCHAR(200)  NOT NULL,
	PRIMARY KEY (book_id)
);

CREATE TABLE Wishlist(
	wishlist_id  INT  NOT NULL AUTO_INCREMENT, 
	user_id  INT, 
	book_id  INT, 
	PRIMARY KEY (wishlist_id),
	CONSTRAINT fk_user
	FOREIGN KEY (user_id)
		REFERENCES UserAccount(user_id),
	CONSTRAINT fk_book
	FOREIGN KEY (book_id)
		REFERENCES Books(book_id)
);


CREATE TABLE Stores(
	store_id  INT NOT NULL, 
	locale  VARCHAR(500)  NOT NULL, 
	PRIMARY KEY (store_id)
);


INSERT INTO Books VALUES(9150,
						"I Know Why The Caged Bird Sings",
						"auto-biography",
						"Maya Angelou");

INSERT INTO Books VALUES(9151,
						"Beloved",
						"Fiction",
						"Tony Morrison");

INSERT INTO Books VALUES(9152,
						"For Whom The Bell Tolls",
						"Fiction",
						"Ernest Hemmingway");

INSERT INTO Books VALUES(9153,
						"Pride and Prejudice",
						"Fiction",
						"Jane Austen");

INSERT INTO Books VALUES(9154,
						"The Alchemist",
						"Fiction",
						"Paolo Coehlo");

INSERT INTO Books VALUES(9155,
						"Tuesdays With Morrie",
						"auto-biography",
						"Mitch Albom");

INSERT INTO Books VALUES(9156,
						"Bird by Bird",
						"auto-biography",
						"Anne Lamott");

INSERT INTO Books VALUES(9157,
						"The Tennis Partner",
						"auto-biography",
						"Abraham Verghese");

INSERT INTO Books VALUES(9158,
						"Delivering On Happiness",
						"business",
						"Tony Hsieh");

INSERT INTO Books VALUES(9159,
						"The Prophet",
						"philosophy",
						"Kalil Gibran");

Insert INTO UserAccount VALUES(123,
							 "Jen",
							 "King",
							 "jking02@gmail.com");

Insert INTO UserAccount VALUES(124,
							 "James",
							 "Gosselin",
							 "JGOSS79@hotmail.com");

Insert INTO UserAccount VALUES(125,
							 "Aaron",
							 "Dailey",
							 "adailey4578@gmail.com");

Insert INTO UserAccount VALUES(126,
							 "Sarah",
							 "Kinnamen",
							 "skalla31@gmail.com");

Insert INTO Stores VALUES(01,
						"2315 N 49th. St Omaha NE 68105");

