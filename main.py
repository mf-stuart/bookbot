from stats import get_book_length, get_char_dict, get_sorted_dict_list, print_char_count

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    return file_content

def main():
    print(
"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt..."""
)

    text = get_book_text()
    get_book_length(text)
    char_dict = get_char_dict(text)
    dict_list = get_sorted_dict_list(char_dict)
    print_char_count(dict_list)


main()