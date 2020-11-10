"""this is Book class for save_content and content_handler."""


class Book:
    """class Book."""

    name: str
    genre_name: str
    author_name: str
    reader_name: str
    description: str
    book_url: str

    def __init__(
            self, name: str,
            genre_name: str,
            author_name: str,
            reader_name: str,
            description: str,
            book_url: str):
        """Save_content.py and content_handler.py constructor."""
        self.name = name
        self.genre_name = genre_name
        self.author_name = author_name
        self.reader_name = reader_name
        self.description = description
        self.book_url = book_url
