"""this is content_saver.py. is save content to file."""

import json

from config import PATH_TO_OUTPUT_FILE


def save_to_file(items: list):
    """Receives content from parser.py and saves it to a file."""
    with open(PATH_TO_OUTPUT_FILE, 'w', newline='', encoding='utf-8') as output_file:
        output_file.write(json.dumps([item.__dict__ for item in items],
                                     ensure_ascii=False,
                                     indent=4))
