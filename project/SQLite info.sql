-- SQLite
SELECT id, data, user_id
FROM closet;


SELECT * FROM closet;

create table closets(
    id TEXT NOT NULL PRIMARY KEY,
    user_id TEXT NOT NULL,
    closet_name TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_info (id)
)