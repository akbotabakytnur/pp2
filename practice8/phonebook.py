from connect import connect


def search_contacts(conn):
    pattern = input("Enter name or phone: ")

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM search_contacts(%s);",
            (pattern,)
        )

        results = cur.fetchall()

        if results:
            for row in results:
                print(row)
        else:
            print("No contacts found")


def add_contact(conn):
    name = input("Enter username: ")
    phone = input("Enter phone: ")

    with conn.cursor() as cur:
        cur.execute(
            "CALL add_or_update_contact(%s, %s);",
            (name, phone)
        )

    conn.commit()
    print("Contact added/updated")


def show_contacts(conn):
    limit = int(input("Number of contacts per page: "))
    page = int(input("Page number: "))

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM get_contacts_paginated(%s, %s);",
            (limit, page)
        )

        contacts = cur.fetchall()

        for contact in contacts:
            print(contact)


def delete_contact(conn):
    value = input("Enter username or phone to delete: ")

    with conn.cursor() as cur:
        cur.execute(
            "CALL delete_contact(%s);",
            (value,)
        )

    conn.commit()
    print("Contact deleted")


def main():

    conn = connect()

    if conn is None:
        return

    while True:

        print("""
====== PhoneBook ======

1. Search contact
2. Add/update contact
3. Show contacts
4. Delete contact
5. Exit
""")

        choice = input("Choose option: ")

        if choice == "1":
            search_contacts(conn)

        elif choice == "2":
            add_contact(conn)

        elif choice == "3":
            show_contacts(conn)

        elif choice == "4":
            delete_contact(conn)

        elif choice == "5":
            print("Goodbye!")
            conn.close()
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()