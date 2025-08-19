import sys
from stats import count_words
from stats import count_characters
from stats import list_characters

def get_book_text(filepath = ""):
    with open(filepath) as f:
        file = f.read()
        return file
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        location = sys.argv[1]
        book = get_book_text(location)
        num_words = count_words(book)
        characters = count_characters(book)
        sorted_characters = (list_characters(characters))

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {location}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in sorted_characters:
            if char["char"].isalpha():
                print(f"{char["char"]}: {char["num"]}")
        print("============= END ===============")

main()