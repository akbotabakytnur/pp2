CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    contact_id_value INTEGER;
BEGIN

    -- Find contact id
    SELECT id INTO contact_id_value
    FROM contacts
    WHERE username = p_contact_name;


    -- If contact exists, add phone
    IF contact_id_value IS NOT NULL THEN

        INSERT INTO phones(contact_id, phone, type)
        VALUES(contact_id_value, p_phone, p_type);

    ELSE

        RAISE NOTICE 'Contact not found';

    END IF;

END;
$$;
--2--
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    group_id_value INTEGER;
    contact_id_value INTEGER;
BEGIN

    -- Find or create group
    SELECT id INTO group_id_value
    FROM groups
    WHERE name = p_group_name;


    IF group_id_value IS NULL THEN

        INSERT INTO groups(name)
        VALUES(p_group_name)
        RETURNING id INTO group_id_value;

    END IF;


    -- Find contact
    SELECT id INTO contact_id_value
    FROM contacts
    WHERE username = p_contact_name;


    -- Update contact group
    IF contact_id_value IS NOT NULL THEN

        UPDATE contacts
        SET group_id = group_id_value
        WHERE id = contact_id_value;

    ELSE

        RAISE NOTICE 'Contact not found';

    END IF;

END;
$$;
#search
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id INTEGER,
    username VARCHAR,
    email VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.username,
        c.email,
        p.phone
    FROM contacts c
    LEFT JOIN phones p
        ON c.id = p.contact_id
    WHERE c.username ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;
