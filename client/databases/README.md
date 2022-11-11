# Databases

## Customers :

| **USER**       | type      | constraints     | exemple                |
|----------------|-----------|-----------------|------------------------|
| id             | CHAR(10)  | NOT NULL UNIQUE | "123456789A"           |
| username       | CHAR(30)  | NOT NULL UNIQUE | "bob"                  |
| hased_password | CHAR(100) | NOT NULL        | "oA187a3E..."          |
| email          | CHAR(50)  | NOT NULL UNIQUE | "bob@exemple.com"      |
| created_at     | TIMESTAMP | NOT NULL        | 2022-11-11 17:54:04    |
| chat_list      | CHAR(500) |                 | "EBAENnbj78UAJlfoep78" |

/!\ chat_list "EBAENnbj78UAJlfoep78" :
* chat_id_1 = "EBAENnbj78"
* chat_id_2 = "UAJlfoep78"
<br/>

| **FRIEND_REQUEST** | type                       | constraints | exemple                |
|--------------------|----------------------------|-------------|------------------------|
| from_user_id       | CHAR(10)                   | NOT NULL    | "123456789A"           |
| to_user_id         | CHAR(10)                   | NOT NULL    | "987654321Z"           |
| status             | TINYINT(1)                 | NOT NULL    | 1                      |
| PRIMARY KEY        | (from_user_id, to_user_id) | UNIQUE      | "123456789A987654321Z" |

| **MUTAL_FIREND** | type                   | constraints | exemple                |
|------------------|------------------------|-------------|------------------------|
| user_id_1        | CHAR(10)               | NOT NULL    | "123456789A"           |
| user_id_2        | CHAR(10)               | NOT NULL    | "987654321Z"           |
| PRIMARY KEY      | (user_id_1, user_id_2) | UNIQUE      | "123456789A987654321Z" |


## Messages :

| **INDEX**  | type      | constraints     | exemple                |
|------------|-----------|-----------------|------------------------|
|  chat_id   | CHAR(10)  | UNIQUE NOT NULL | "ABCD123456"           |
| user_list  | CHAR(500) | NOT NULL        | "123456789A987654321Z" |
| created_at | TIMESTAMP | NOT NULL        | 2022-11-11 18:28:06    |

/!\ user_list "123456789A987654321Z" :
* user_id_1 = "123456789A"
* user_id_2 = "987654321Z"
<br/>

| **CHAT_ID** | type        | constraints | exemple             |
|-------------|-------------|-------------|---------------------|
| id          | PRIMARY KEY | NOT NULL    | 87                  |
| user_id     | CHAR(10)    | NOT NULL    | "123456789A"        |
| content     | CHAR(500)   | NOT NULL    | "Hello world!"      |
| created_at  | TIMESTAMP   | NOT NULL    | 2022-11-11 18:32:17 |
