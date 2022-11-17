import sqlite3
import os


def create_db_customers():
    if os.path.isfile("customers.sqlite"):
        raise FileExistsError

    customers = sqlite3.connect("customers.sqlite")
    customers_cursor = customers.cursor()

    customers_cursor.execute("""
    CREATE TABLE 'user' (
        id CHAR(10) NOT NULL UNIQUE,
        username CHAR(30) NOT NULL UNIQUE,
        hased_password CHAR(100) NOT NULL,
        email CHAR(50) NOT NULL UNIQUE,
        created_at TIMESTAMP NOT NULL,
        chat_list CHAR(500),
        CONSTRAINT CK_customers_id_length check (length(id) = 10),
        CONSTRAINT CK_customers_username_length check (length(username) > 3),
        CONSTRAINT CK_customers_hased_password_length check (LENGTH(hased_password) > 5),
        CONSTRAINT CK_customers_chat_list_lenght CHECK (LENGTH(chat_list) <= 500)
        );
    """)

    customers_cursor.execute("""
    CREATE TABLE mutal_friend (
        user_id_1 CHAR(10) NOT NULL,
        user_id_2 CHAR(10) NOT NULL,
        PRIMARY KEY (user_id_1, user_id_2),
        CONSTRAINT CK_user_id_1_length CHECK (LENGTH(user_id_1) = 10),
        CONSTRAINT CK_user_id_2_length CHECK (LENGTH(user_id_2) = 10)
        );
    """)

    customers_cursor.execute("""
    CREATE TABLE friend_request (
        from_user_id CHAR(10) NOT NULL,
        to_user_id CHAR(10) NOT NULL,
        status TINYINT(1) NOT NULL,
        PRIMARY KEY (from_user_id, to_user_id),
        CONSTRAINT CK_from_user_id_length CHECK (LENGTH(from_user_id) = 10),
        CONSTRAINT CK_to_user_id_length CHECK (LENGTH(to_user_id) = 10)
        CONSTRAINT CK_status_length CHECK (LENGTH(status) = 1)
        );
    """)


def create_db_messages():
    if os.path.isfile("messages.sqlite"):
        raise FileExistsError

    messages = sqlite3.connect("messages.sqlite")
    messages_cursor = messages.cursor()

    messages_cursor.execute("""
    CREATE TABLE 'index' (
        chat_id CHAR(10) UNIQUE NOT NULL,
        user_list CHAR(500) NOT NULL,
        created_at TIMESTAMP NOT NULL,
        CONSTRAINT CK_chat_id_length CHECK (LENGTH(chat_id) = 10),
        CONSTRAINT CK_user_list_max CHECK (LENGTH(user_list) <= 500)
        );
    """)

create_db_customers()
create_db_messages()