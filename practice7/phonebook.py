import csv
import psycopg2
from connect import connect


def create_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL
    );
    """

    with conn.cursor() as cur:
        cur.execute(create_table_sql)

    conn.commit()
    print("Table created successfully!")


def insert_from_console(conn):
    username = input("Enter username: ")
    phone = input("Enter phone number: ")

    insert_sql = """
    INSERT INTO contacts (username, phone)
    VALUES (%s, %s)
    """

    with conn.cursor() as cur:
        cur.execute(insert_sql, (username, phone))

    conn.commit()
    print("Contact added successfully!")


def insert_from_csv(conn):
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)

        insert_sql = """
        INSERT INTO contacts (username, phone)
        VALUES (%s, %s)
        """

        with conn.cursor() as cur:
            for row in reader:
                cur.execute(insert_sql, (row[0], row[1]))

    conn.commit()
    print("Contacts imported successfully!")


def query_contacts(conn):
    print("\n1. Search by username")
    print("2. Search by phone prefix")

    choice = input("Choose: ")

    with conn.cursor() as cur:

        if choice == "1":
            username = input("Enter username: ")

            cur.execute(
                "SELECT * FROM contacts WHERE username = %s",
                (username,)
            )

        elif choice == "2":
            phone = input("Enter phone prefix: ")

            cur.execute(
                "SELECT * FROM contacts WHERE phone LIKE %s",
                (phone + "%",)
            )

        else:
            print("Invalid choice!")
            return

        contacts = cur.fetchall()

    if contacts:
        print("\nContacts:")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")


def update_contact(conn):
    username = input("Enter username: ")
    new_phone = input("Enter new phone number: ")

    update_sql = """
    UPDATE contacts
    SET phone = %s
    WHERE username = %s
    """

    with conn.cursor() as cur:
        cur.execute(update_sql, (new_phone, username))

    conn.commit()
    print("Contact updated successfully!")


def delete_contact(conn):
    username = input("Enter username to delete: ")

    delete_sql = """
    DELETE FROM contacts
    WHERE username = %s
    """

    with conn.cursor() as cur:
        cur.execute(delete_sql, (username,))

    conn.commit()
    print("Contact deleted successfully!")


def main():
    conn = connect()

    create_table(conn)

    while True:
        print("\n====== PHONEBOOK ======")
        print("1. Add contact")
        print("2. Import contacts from CSV")
        print("3. Search contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_console(conn)

        elif choice == "2":
            insert_from_csv(conn)

        elif choice == "3":
            query_contacts(conn)

        elif choice == "4":
            update_contact(conn)

        elif choice == "5":
            delete_contact(conn)

        elif choice == "6":
            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()