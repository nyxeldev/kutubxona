def load_books(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def find_book(books, title):
    for b in books:
        if title.lower() in b.lower():
            return b
    return None
