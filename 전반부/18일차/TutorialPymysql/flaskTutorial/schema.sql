DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
    id int(11) NOT NULL AUTO_INCREMENT,
	username varchar(50) NOT NULL,
	password varchar(200) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE post (
    id int(11) NOT NULL AUTO_INCREMENT,
    author_id int(11) NOT NULL,
    created timestamp NOT NULL DEFAULT current_timestamp(),
    title varchar(50) NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id),
    PRIMARY KEY (id)
);