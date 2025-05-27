from stats import get_book_length, get_char_dict, get_sorted_dict_list, print_char_count
import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    try:
        path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(
f"""
============ BOOKBOT ============
Analyzing book found at {path}..."""
)

    text = get_book_text(path)
    get_book_length(text)
    char_dict = get_char_dict(text)
    dict_list = get_sorted_dict_list(char_dict)
    print_char_count(dict_list)


main()