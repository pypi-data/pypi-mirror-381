import urllib.request

import pytest

from berea.bible import BibleClient, BibleInputError



def valid_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return True
            else:
                return False
    except urllib.error.HTTPError as e:
        print("HTTP error:", e.code)
        return False
    except urllib.error.URLError as e:
        print("URL error:", e.reason)
        return False


@pytest.mark.parametrize(
    "msg, book, chapter, verse, translation, expected_link",
    [
        (
            "Creating link for a single verse failed",
            "John", "3", "16", "BSB",
            "https://www.stepbible.org/?q=version=BSB@reference=john.3.16&options=NVHUG"
        ),
        (
            "Creating link for multiple verses failed",
            "John", "3", "16-18", "BSB",
            "https://www.stepbible.org/?q=version=BSB@reference=john.3.16-john.3.18&options=NVHUG"
        ),
        (
            "Creating link for a chapter failed",
            "Psalms", "117", None, "BSB",
            "https://www.stepbible.org/?q=version=BSB@reference=psalm.117&options=NVHUG"
        ),
        (
            "Creating link for a book",
            "III John", None, None, "BSB",
            "https://www.stepbible.org/?q=version=BSB@reference=3john&options=NVHUG"
        ),
    ]
)
def test_create_link(msg, book, chapter, verse, translation, expected_link):
    bible = BibleClient(translation)
    actual_link = bible.create_link(book, chapter, verse)
    assert actual_link == expected_link, msg
    assert valid_url(actual_link)


def test_validate_resource_abbreviations():
    """Creating links from the resource's book abbreviations yields valid URLs."""
    bible = BibleClient('BSB')
    
    books = bible.get_bible_cursor().execute("SELECT * FROM books").fetchall()
    
    for book in books:
        link = bible.create_link(book['name'])
        assert valid_url(link), f"{book['name']} produced invalid link: {link}"


@pytest.mark.parametrize(
    "translation",
    [
        ('KJV'),
        ('BSB'),
        ('RLT'),        
        ('UKJV'),        
    ]
)
def test_create_bible_db(translation):
    bible = BibleClient(translation)
    bible.create_bible_db()

    cursor = bible.get_bible_cursor()

    msg = 'Downloading the translation database failed.'
    assert pytest.translation_exists(translation), msg

    sql = "SELECT name FROM sqlite_master WHERE type='table';"
    actual_tables = [row['name'] for row in cursor.execute(sql).fetchall()]

    table_record_counts = {
        'books': 66,
        'verses': 31102,
    }

    msg = 'Renaming the database tables failed.'
    renamed_tables = table_record_counts.keys()
    assert set(renamed_tables).issubset(actual_tables), msg

    for table, expected_records_count in table_record_counts.items():
        sql = f"SELECT COUNT(*) FROM {table};"
        actual_records_count = cursor.execute(sql).fetchone()[0]
        
        msg = f"'{table}' table does not contain expected record count."
        assert actual_records_count == expected_records_count, msg

    created_tables = ['abbreviations', 'resources', 'resources_abbreviations']
    for expected_table in created_tables:
        msg =  f"'{expected_table}' table does not exist."
        assert expected_table in actual_tables, msg


def test_search_testament_error():
    """This error is only reachable from BibleClient.
    """
    bible = BibleClient('BSB')
    
    with pytest.raises(BibleInputError, match="Invalid testament='secret'."):
        bible.search_testament("That's all folks!", "secret")
