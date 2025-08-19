def count_words(book_text = ""):
    book_list = book_text.split()
    word_count = len(book_list)
    return word_count

def count_characters(book_text = ""):
    book = book_text.lower()
    characters = {}
    for character in book:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(items):
    return items["num"]

def list_characters(characters):
    char_list = []
    for character in characters:
        count = characters[character]
        new_char = {"char":character, "num": count}
        char_list.append(new_char)
    char_list.sort(reverse=True, key=sort_on)
    return char_list