from stats import count_words
from stats import count_characters

def get_book_text(filepath = ""):
    with open(filepath) as f:
        file = f.read()
        return file
    
def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    print(f"{num_words} words found in the document")
    characters = count_characters(book)
    print(characters)

main()