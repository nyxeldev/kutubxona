from utils import load_books


def main():
    books = load_books("books.txt")
    print(f"Kutubxonada {len(books)} ta kitob bor")
    for b in books:
        print(" -", b)


if __name__ == "__main__":
    main()
