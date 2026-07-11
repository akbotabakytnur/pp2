CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE (
    id INTEGER,
    username VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.username, c.phone
    FROM contacts c
    WHERE c.username ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
#2
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    page_size INTEGER,
    page_number INTEGER
)
RETURNS TABLE (
    id INTEGER,
    username VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN

    RETURN QUERY
    SELECT c.id, c.username, c.phone
    FROM contacts c
    ORDER BY c.id
    LIMIT page_size
    OFFSET (page_number - 1) * page_size;

END;
$$ LANGUAGE plpgsql;