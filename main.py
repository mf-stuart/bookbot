from stats import get_book_length, get_char_dict

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    return file_content

def main():
    text = get_book_text()
    get_book_length(text)
    char_dict = get_char_dict(text)
    print(char_dict)

main()