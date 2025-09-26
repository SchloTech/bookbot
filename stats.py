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
    
    list_of_dicts = [{"name": key, "num": value} for key, value in dictionary.items()]

    def sort_on(items):
        return items["num"]
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
