CREATE TABLE user_info (
    id TEXT NOT NULL PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    userName TEXT NOT NULL,
    pwd TEXT NOT NULL
);

DROP TABLE closet;

CREATE TABLE closet (
    id TEXT NOT NULL PRIMARY KEY,
    user_id TEXT NOT NULL,
    closet_name TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_info (id)
);

DROP TABLE items;
DROP TABLE item;

CREATE TABLE item (
    id TEXT NOT NULL PRIMARY KEY,
    category TEXT NOT NULL,
    color TEXT NOT NULL,
    season TEXT NOT NULL,
    style TEXT NOT NULL,
    fit TEXT NOT NULL,
    FOREIGN KEY (closet_id) REFERENCES closet (id)
)

