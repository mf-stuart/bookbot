def get_book_length(text):
    text_list = text.split()
    num_words = len(text_list)
    print(f"{num_words} words found in the document")

def get_char_dict(text):
    char_dict = dict()
    for char in text:
        char_dict[char.lower()] = char_dict.get(char.lower(), 0) + 1
    return char_dict