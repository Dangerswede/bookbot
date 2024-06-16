def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print_report(num_words, num_characters)
    

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

def print_report(num_words, num_characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    
    
    character_list = list(num_characters.items())
    character_list.sort(key=lambda item: item[1], reverse=True)

    for char, count in character_list:
        if char.isalpha() == True:
            print(f"the '{char}'  character was found {count} times")
    print("--- End report ---")
main()