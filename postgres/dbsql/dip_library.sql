CREATE database dip_library;

\c dip_library

CREATE TABLE midaechul_rec (
    isbn13 VARCHAR(13) PRIMARY KEY,
    nei_1 VARCHAR(13) NOT NULL,
    nei_2 VARCHAR(13) NOT NULL,
    nei_3 VARCHAR(13) NOT NULL,
    nei_imgurl_1 VARCHAR(200) ,
    nei_imgurl_2 VARCHAR(200) ,
    nei_imgurl_3 VARCHAR(200) ,
    nei_bookname_1 VARCHAR(400) NOT NULL,
    nei_bookname_2 VARCHAR(400) NOT NULL,
    nei_bookname_3 VARCHAR(400) NOT NULL
);

CREATE TABLE midaechul_gender_age (
    isbn13 VARCHAR(13) PRIMARY KEY,
    gender VARCHAR(2) NOT NULL,
    age INT NOT NULL,
    bukbu INT NOT NULL,
    dalseochild INT NOT NULL,
    dowon INT NOT NULL,
    bonly INT NOT NULL,
    sungseo INT NOT NULL,
    topic INT NOT NULL,
    bookname VARCHAR(400) NOT NULL,
    bookurl VARCHAR(200)
);

COPY midaechul_rec
FROM '/tmp/midaechul_rec.csv'
DELIMITER ','
CSV HEADER;

COPY midaechul_gender_age
FROM '/tmp/midaechul_gender_age_topic.csv'
DELIMITER ','
CSV HEADER;
