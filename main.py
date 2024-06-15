def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_string = get_lowered_string(text)
    print(f"{num_words} words found in the document")

def get_lowered_string(text):
    lowered_text = text.lower()
    return (lowered_text)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()