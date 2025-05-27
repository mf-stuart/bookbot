def get_book_length(text):
    print("----------- Word Count ----------")
    text_list = text.split()
    num_words = len(text_list)
    print(f"Found {num_words} total words")

def get_char_dict(text):
    char_dict = dict()
    for char in text:
        char_dict[char.lower()] = char_dict.get(char.lower(), 0) + 1
    return char_dict

def get_sorted_dict_list(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list



def print_char_count(dict_list):
    print("--------- Character Count -------")
    for entry in dict_list:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
