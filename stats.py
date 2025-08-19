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