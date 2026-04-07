CREATE OR REPLACE FUNCTION duplicate_records()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
	INSERT INTO aaab(bbba, ccca)
	VALUES (NEW.bbb, NEW.ccc);
	RETURN NEW;
END
$$;

CREATE TRIGGER aaa_changes
	BEFORE INSERT
	ON aaa
	FOR EACH ROW
	EXECUTE PROCEDURE duplicate_records();

INSERT INTO aaa(bbb, ccc)
VALUES ('abcde', 'efghi');










	