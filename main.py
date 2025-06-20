import sys
from stats import count_words
from stats import count_chars
from stats import sort_dict

def get_book_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        res = get_book_text(sys.argv[1])
        word_count = count_words(res)
        char_count_dict = count_chars(res)
        sorted_list = sort_dict(char_count_dict)    

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("----------- Char Count ----------")
        
        for e in sorted_list:
            if e["char"].isalpha():
                print(f"{e['char']}: {e['num']}")

main()
