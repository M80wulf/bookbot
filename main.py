import  sys
from stats import get_num_words, character_count, sort_count
DEBUG = True

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

    return book_content
def main():
    if len(sys.argv) == 2:
        if DEBUG: print(f"DEBUG: running argument = {sys.argv}")
        path = sys.argv[1]
    else:
        sys.exit("Usage: python3 main.py <path_to_book>")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)
    word_count = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    chars = character_count(text)
    sorted_chars = sort_count(chars)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")






main()

