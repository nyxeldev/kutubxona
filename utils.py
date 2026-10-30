def load_books(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
