import sqlite3
import urllib.request
from urllib.error import HTTPError
import json
import csv
import sys
import os

from berea.utils import get_source_root, get_app_data_path


def clean_book_name(book):
        cleaned_name = book.title()
        # Database names use proper title case
        # eg. 'Song of Solomon' and 'Revelation of John'
        if 'Of' in cleaned_name:
            cleaned_name = cleaned_name.replace('Of', 'of')
        return cleaned_name


def import_resource_books(resource='step_bible'):
    books = []
    
    with open(f'{get_source_root()}/data/{resource}_books.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            books.append(row['abbreviation'])
    
    return books


def parse_verses_str(verses):
    verses_split = verses.split('-')
    return verses_split[0], verses_split[1]


def list_to_sql(data):
    return "('" + "','".join(data) + "')"


class BibleInputError(ValueError):
    pass


class BibleClient:
    def __init__(self, translation):
        self.translation = translation
        # Use venv path or platform app data path to store translation DBs
        self.database = f"{get_app_data_path('translations')}/{self.translation}.db"
    
    # TODO: Download from a fork
    def download_raw_bible(self):
        url = f"https://github.com/scrollmapper/bible_databases/raw/refs/heads/master/formats/sqlite/{self.translation}.db"

        try:
            urllib.request.urlretrieve(url, self.database)
            return f"Downloaded: {self.database}"
            
        except HTTPError:
            link = "https://github.com/scrollmapper/bible_databases?tab=readme-ov-file#available-translations-140"
            msg = (
                f"Translation '{self.translation}' does not exist.\n"
                f"Check the following link for available translations:\n{link}"
            )
            raise BibleInputError(msg)
    
    # TODO: Close out the conn when it's released
    def get_bible_cursor(self):
        conn = sqlite3.connect(self.database)
        conn.row_factory = sqlite3.Row
        # TODO: Use context manager?
        return conn.cursor()
    
    def rename_tables(self):
        """Rename tables for consistent schema across downloaded translations.
        """
        cursor = self.get_bible_cursor()
        
        tables = ['books', 'verses']
        for table in tables:
            # SQLite doesn't bind parameters for schema objects
            sql = f"ALTER TABLE {self.translation}_{table} RENAME TO {table};"
            cursor.execute(sql)
    
    def create_abbreviations_table(self):
        cursor = self.get_bible_cursor()

        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS abbreviations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            abbreviation TEXT,
            FOREIGN KEY (book_id) REFERENCES books(id)
        );
        """)
        
        books_to_abbreviations = {}
        
        with open(f'{get_source_root()}/data/book_abbreviations.json') as file:
            books_to_abbreviations = dict(json.load(file))
    
        # Create a conn to commit inserts and close 
        conn = sqlite3.connect(self.database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        for book, abbreviations in books_to_abbreviations.items():
            for abbreviation in abbreviations:
                params = {
                    'abbreviation': abbreviation,
                    'book': book,
                }
                
                cursor.execute(f"""
                INSERT INTO abbreviations (abbreviation, book_id)
                SELECT :abbreviation, books.id
                FROM books
                WHERE books.name = :book;
                """, params)
        
        conn.commit()
        conn.close()

    def create_resource_tables(self):
        cursor = self.get_bible_cursor()

        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
        """)
        
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS resources_abbreviations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resource_id INTEGER,
            abbreviation_id INTEGER
        );
        """)
        
        # Create a conn to commit inserts and close 
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        
        # TODO: Insert STEP Bible dynamically
        resource='STEP Bible'
        cursor.execute(f"""
        INSERT INTO resources (name) VALUES (
            'STEP Bible'
        );
        """)
        
        conn.commit()
        conn.close()
        
        abbreviations = import_resource_books()
        
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        
        for abbreviation in abbreviations:
            params = {
                'abbreviation': abbreviation.lower(),
            }
            
            # TODO: Select STEP Bible id dynamically
            cursor.execute(f"""
            INSERT INTO resources_abbreviations (resource_id, abbreviation_id)
            SELECT 1, abbreviations.id
            FROM abbreviations
            WHERE abbreviations.abbreviation = :abbreviation;
            """, params)
        
        conn.commit()
        conn.close()
    
    def create_bible_db(self):
        self.download_raw_bible()
        self.rename_tables()
        self.create_abbreviations_table()
        self.create_resource_tables()
    
    def delete_translation(self):
        os.remove(self.database)
        return f"Deleted transation '{self.translation}'."
    
    def get_book_abbreviation_by_resource(self, book, resource):
        """Get a book's abbreviation used by a specific resource.
        """
        cursor = self.get_bible_cursor()
   
        params = {
            'book': book,
            'resource': resource,
        }
        
        cursor.execute("""
            SELECT abbreviation FROM abbreviations
            JOIN books ON abbreviations.book_id = books.id
            JOIN resources_abbreviations ON resources_abbreviations.abbreviation_id = abbreviations.id
            JOIN resources ON resources_abbreviations.resource_id = resources.id
            WHERE books.name = :book
            AND resources.name = :resource
            """, params)
        
        # BUG: why is this failing? stale cursor from previous SELECT?
        # Assuming a resource only has one abbreviation for a given book and translation
        return cursor.fetchone()[0]
    
    def get_book_from_abbreviation(self, book):
        cleaned_book_name = clean_book_name(book)
        cursor = self.get_bible_cursor()
        
        # Use full book name if that was passed in
        book_row = cursor.execute(
            """SELECT * FROM books WHERE books.name = ?;""",
            (cleaned_book_name,)).fetchone()
        
        if book_row:
            return cleaned_book_name
        
        # Get full book name using abbreviation
        else:
            book_row = cursor.execute("""
            SELECT * FROM books
            JOIN abbreviations ON abbreviations.book_id = books.id
            WHERE abbreviations.abbreviation = ?;
            """, (book,)).fetchone()
            
            if book_row:
                return book_row['name']
            else:
                raise BibleInputError(f"Invalid input {book=}.")
    
    # TODO: Link format depends on resource
    def create_link(self, book, chapter=None, verse=None, resource='STEP Bible'):
        book_abbrev = self.get_book_abbreviation_by_resource(book, resource)
        
        link = ''
        
        if verse:
            # Parse verses if multiple provided
            if '-' in verse:
                verse_start, verse_end = parse_verses_str(verse)
                link = f"https://www.stepbible.org/?q=version={self.translation}@reference={book_abbrev}.{chapter}.{verse_start}-{book_abbrev}.{chapter}.{verse_end}&options=NVHUG"
                
            else:
                link = f"https://www.stepbible.org/?q=version={self.translation}@reference={book_abbrev}.{chapter}.{verse}&options=NVHUG"
        
        elif chapter:
            link = f"https://www.stepbible.org/?q=version={self.translation}@reference={book_abbrev}.{chapter}&options=NVHUG"
        
        # Make link for whole book
        else:
            link = f"https://www.stepbible.org/?q=version={self.translation}@reference={book_abbrev}&options=NVHUG"

        return link

    def get_verses_by_book(self, book):
        cursor = self.get_bible_cursor()
        book = self.get_book_from_abbreviation(book)
        params = {'book': book}
    
        cursor.execute("""
        SELECT verse, text FROM verses
        JOIN books ON verses.book_id = books.id
        WHERE books.name = :book
        """, params)

        verse_records = cursor.fetchall()
        
        return verse_records

    # TODO: Validate chapter?
    def get_verses_by_chapter(self, book, chapter):
        cursor = self.get_bible_cursor()
        book = self.get_book_from_abbreviation(book)
        params = {'book': book, 'chapter': chapter}
        
        cursor.execute("""
        SELECT verse, text FROM verses
        JOIN books ON verses.book_id = books.id
        WHERE books.name = :book
        AND chapter = :chapter
        """, params)

        verse_records = cursor.fetchall()
        
        if len(verse_records) == 0:
            raise BibleInputError(f"Invalid chapter: {book} {chapter}.")
        
        else:
            return verse_records

    # TODO: Validate chapter?
    def get_verse(self, book, chapter, verse):
        cursor = self.get_bible_cursor()
        book = self.get_book_from_abbreviation(book)
        params = {
            'book': book,
            'chapter': chapter,
            'verse': verse
        }
        
        cursor.execute("""
        SELECT verse, text FROM verses
        JOIN books ON verses.book_id = books.id
        WHERE books.name = :book
        AND chapter = :chapter
        AND verse = :verse
        """, params)

        verse_records = cursor.fetchall()
        
        if len(verse_records) == 0:
            raise BibleInputError(f"Invalid verse: {book} {chapter}:{verse}.")
        
        else:
            return verse_records

    # TODO: Validate chapter?
    def get_verses(self, book, chapter, verse):
        """
        Print a range of verses, eg. 5-7. 
        """
        cursor = self.get_bible_cursor()
        book = self.get_book_from_abbreviation(book)
        verse_start, verse_end = parse_verses_str(verse)
        
        params = {
            'book': book,
            'chapter': chapter,
            'verse_start': verse_start,
            'verse_end': verse_end,
        }
        
        cursor.execute("""
        SELECT verse, text FROM verses
        JOIN books ON verses.book_id = books.id
        WHERE books.name = :book
        AND chapter = :chapter
        AND verse BETWEEN :verse_start AND :verse_end
        """, params)

        verse_records = cursor.fetchall()
        
        if len(verse_records) == 0:
            raise BibleInputError(
                f"Invalid verses: {book} "
                f"{chapter}:{verse_start}-{verse_end}."
            )
        
        else:
            return verse_records
    
    # TODO: Output txt, markdown table, csv format
    def search_bible(self, phrase):
        cursor = self.get_bible_cursor()
        
        cursor.execute("""
        SELECT books.name AS book, chapter, verse, text FROM verses
        JOIN books ON verses.book_id = books.id
        WHERE verses.text LIKE ?;
        """, (f"%{phrase}%",))
        
        return cursor.fetchall()
    
    def search_testament(self, phrase, testament):
        cursor = self.get_bible_cursor()

        new_testament = [
            'Matthew',
            'Mark',
            'Luke',
            'John',
            'Acts',
            'Romans',
            'I Corinthians',
            'II Corinthians',
            'Galatians',
            'Ephesians',
            'Philippians',
            'Colossians',
            'I Thessalonians',
            'II Thessalonians',
            'I Timothy',
            'II Timothy',
            'Titus',
            'Philemon',
            'Hebrews',
            'James',
            'I Peter',
            'II Peter',
            'I John',
            'II John',
            'III John',
            'Jude',
            'Revelation of John'
        ]

        nt_sql_list = list_to_sql(new_testament)

        if testament == 'nt':

            sql = f"""
            SELECT books.name AS book, chapter, verse, text FROM verses
            JOIN books ON verses.book_id = books.id
            WHERE verses.text LIKE ?
            AND books.name IN {nt_sql_list};
            """
        
        elif testament == 'ot': 

            sql = f"""
            SELECT books.name AS book, chapter, verse, text FROM verses
            JOIN books ON verses.book_id = books.id
            WHERE verses.text LIKE ?
            AND books.name NOT IN {nt_sql_list};
            """
        
        else:
            raise BibleInputError(f"Invalid {testament=}.")
        
        # Bind phrase since it's user input
        cursor.execute(sql, (f"%{phrase}%",))
        return cursor.fetchall()
    
    def search_book(self, phrase, book):
        cursor = self.get_bible_cursor()

        book = self.get_book_from_abbreviation(book)
        params = {
            'phrase': f"%{phrase}%",
            'book': book,
            }
        
        cursor.execute("""
        SELECT books.name AS book, chapter, verse, text FROM verses
        JOIN books ON verses.book_id = books.id
        WHERE verses.text LIKE :phrase
        AND book = :book;
        """, params)
        
        return cursor.fetchall()

    # TODO: Validate chapter?
    def search_chapter(self, phrase, book, chapter):
        cursor = self.get_bible_cursor()

        book = self.get_book_from_abbreviation(book)
        params = {
            'phrase': f"%{phrase}%",
            'book': book,
            'chapter': chapter,
            }
        
        cursor.execute("""
        SELECT books.name AS book, chapter, verse, text FROM verses
        JOIN books ON verses.book_id = books.id
        WHERE verses.text LIKE :phrase
        AND book = :book
        AND chapter = :chapter;
        """, params)
        
        return cursor.fetchall()
