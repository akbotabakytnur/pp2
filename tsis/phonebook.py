from connect import connect
import json


def search_contacts(conn):
    query = input("Search: ")

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM search_contacts(%s);",
            (query,)
        )

        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No contacts found")


def add_phone(conn):
    name = input("Contact name: ")
    phone = input("Phone: ")
    phone_type = input("Type (home/work/mobile): ")

    with conn.cursor() as cur:
        cur.execute(
            "CALL add_phone(%s, %s, %s);",
            (name, phone, phone_type)
        )

    conn.commit()
    print("Phone added")


def move_group(conn):
    name = input("Contact name: ")
    group = input("New group: ")

    with conn.cursor() as cur:
        cur.execute(
            "CALL move_to_group(%s, %s);",
            (name, group)
        )

    conn.commit()
    print("Group updated")


def filter_group(conn):
    group = input("Group name: ")

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT 
                c.username,
                c.email,
                c.birthday,
                g.name
            FROM contacts c
            JOIN groups g
            ON c.group_id = g.id
            WHERE g.name = %s;
            """,
            (group,)
        )

        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No contacts in this group")


def show_contacts(conn):

    limit = int(input("Contacts per page: "))
    offset = int(input("Offset: "))

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM get_contacts_paginated(%s, %s);",
            (limit, offset)
        )

        rows = cur.fetchall()

        for row in rows:
            print(row)


def export_json(conn):

    with conn.cursor() as cur:

        cur.execute(
            """
            SELECT 
                c.username,
                c.email,
                c.birthday,
                g.name
            FROM contacts c
            LEFT JOIN groups g
            ON c.group_id = g.id;
            """
        )

        contacts = []

        for row in cur.fetchall():
            contacts.append(
                {
                    "name": row[0],
                    "email": row[1],
                    "birthday": str(row[2]) if row[2] else None,
                    "group": row[3]
                }
            )


    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    print("JSON export finished")


def import_json(conn):

    try:

        with open("contacts.json", "r") as file:
            contacts = json.load(file)


        with conn.cursor() as cur:

            for contact in contacts:

                name = contact["name"]
                email = contact.get("email")
                birthday = contact.get("birthday")


                cur.execute(
                    """
                    SELECT id 
                    FROM contacts
                    WHERE username = %s;
                    """,
                    (name,)
                )

                exists = cur.fetchone()


                if exists:

                    choice = input(
                        f"{name} already exists. Skip or overwrite? (s/o): "
                    )


                    if choice.lower() == "s":
                        continue


                    cur.execute(
                        """
                        UPDATE contacts
                        SET email = %s,
                            birthday = %s
                        WHERE username = %s;
                        """,
                        (email, birthday, name)
                    )


                else:

                    cur.execute(
                        """
                        INSERT INTO contacts(
                            username,
                            email,
                            birthday
                        )
                        VALUES(%s, %s, %s);
                        """,
                        (name, email, birthday)
                    )


        conn.commit()

        print("JSON import finished")


    except FileNotFoundError:
        print("contacts.json file not found")


    except Exception as e:
        print("Error:", e)
        conn.rollback()



def main():

    conn = connect()

    if conn is None:
        print("Database connection failed")
        return


    while True:

        print("""
========== PhoneBook ==========

1. Search contact
2. Add phone
3. Move contact to group
4. Filter by group
5. Export JSON
6. Import JSON
7. Show contacts
8. Exit

===============================
""")


        choice = input("Choose option: ")


        if choice == "1":
            search_contacts(conn)


        elif choice == "2":
            add_phone(conn)


        elif choice == "3":
            move_group(conn)


        elif choice == "4":
            filter_group(conn)


        elif choice == "5":
            export_json(conn)


        elif choice == "6":
            import_json(conn)


        elif choice == "7":
            show_contacts(conn)


        elif choice == "8":
            conn.close()
            print("Goodbye")
            break


        else:
            print("Wrong option")



if __name__ == "__main__":
    main()