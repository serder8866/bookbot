from stats import word_number
from stats import count_char
from stats import sort_dict
import sys

def get_book_text(filepath: str) -> str:
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(filepath) as f:
        return f.read()

    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
    character_count = count_char(text)
    sorted_count = sort_dict(character_count)
    print(f"Found {word_number(text)} total words")
    for item in sorted_count:
        print(f"{item["character"]}: {item["count"]}")

if __name__ == "__main__":
    main()