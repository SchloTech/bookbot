def get_word_count(book_string):
    return len(book_string.split())


def get_character_count(book_string):
    words = book_string.lower()
    character_count = {}

    for letter in words:
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1

    return character_count

def sort_dict(dictionary):
    def sort_on(items):
        return items["num"]
    
    dictionary.sort(reverse=True, key=sort_on)
    return dictionary
