def get_book_text(filepath = ""):
    with open(filepath) as f:
        file = f.read()
        return file
    
def count_words(book_text = ""):
    book_list = book_text.split()
    word_count = len(book_list)
    return word_count
    
def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()