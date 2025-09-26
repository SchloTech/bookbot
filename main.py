from stats import get_word_count, get_character_count, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_string = get_book_text(sys.argv[1])
    num_words = get_word_count(book_string)
    char_count_dict = get_character_count(book_string)
    sorted_char_list_dict = sort_dict(char_count_dict)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

    for item in sorted_char_list_dict:
        if item["name"].isalpha():
            print(f'{item["name"]}: {item["num"]}')

    print("============= END ===============")

main()
