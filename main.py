def main():
    book_path = input("please enter the path of the book you want to analyse: ")
    text = get_book_text(book_path)
    if text == "":
        return
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print_report(num_words, num_characters, book_path)
    
def get_book_text(book_path):
    try: 
        with open(book_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: file at path '{book_path}' was not found.")
        return ""
    
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


def print_report(num_words, num_characters, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    
    character_list = list(num_characters.items())
    character_list.sort(key=lambda item: item[1], reverse=True)

    for char, count in character_list:
        if char.isalpha():
            print(f"the '{char}'  character was found {count} times")
    print("--- End report ---")


main()