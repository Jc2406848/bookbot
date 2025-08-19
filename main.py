from stats import count_words

def get_book_text(filepath = ""):
    with open(filepath) as f:
        file = f.read()
        return file
    
def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()