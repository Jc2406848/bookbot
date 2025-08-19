def get_book_text(filepath = ""):
    with open(filepath) as f:
        file = f.read()
        return file
    
def main():
    print(get_book_text("books/frankenstein.txt"))

main()