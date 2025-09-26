from stats import get_word_count, get_character_count, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_string = get_book_text('./books/frankenstein.txt')
    num_words = get_word_count(book_string)
    char_count_dict = get_character_count(book_string)
    sorted_char_dict = sort_dict(char_count_dict)

    print(f"Found {num_words} total words")
    print(char_count_dict)
    print(sorted_char_dict)

main()
