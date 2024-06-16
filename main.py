def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print(f"{num_words} words found in the document")
    for char in sorted(num_characters):
        print(f"'{char}': {num_characters[char]} characters found in document")

def get_lowered_string(text):
    lowered_text = text.lower()
    return (lowered_text)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    characters = {}
    lowered_text = get_lowered_string(text) 
    for i in lowered_text:
        if i in characters:
            characters[i] += 1
        else: 
            characters[i] = 1
    return characters

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()