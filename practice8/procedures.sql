#1
CREATE OR REPLACE PROCEDURE add_or_update_contact(
    new_username VARCHAR,
    new_phone VARCHAR
)
AS $$
BEGIN

    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE username = new_username
    )
    THEN

        UPDATE contacts
        SET phone = new_phone
        WHERE username = new_username;

    ELSE

        INSERT INTO contacts(username, phone)
        VALUES(new_username, new_phone);

    END IF;

END;
$$ LANGUAGE plpgsql;
#2
-- 2. Bulk Insert with Validation
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_names VARCHAR[], 
    p_phones VARCHAR[],
    INOUT p_errors TEXT[] DEFAULT '{}'
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_length(p_names, 1) LOOP

        -- Check: phone must contain only digits and be at least 7 characters
        IF p_phones[i] ~ '^[0-9]+$' 
           AND length(p_phones[i]) >= 7 THEN

            CALL add_or_update_contact(
                p_names[i], 
                p_phones[i]
            );

        ELSE

            p_errors := array_append(
                p_errors,
                'Invalid: ' || p_names[i] || ' (' || p_phones[i] || ')'
            );

        END IF;

    END LOOP;
END;
$$;
#3
CREATE OR REPLACE PROCEDURE delete_contact(
    search_value VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

    DELETE FROM contacts
    WHERE username = search_value
       OR phone = search_value;

END;
$$;