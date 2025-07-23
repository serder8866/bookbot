from stats import word_number
from stats import count_char

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
    text = get_book_text("books/frankenstein.txt")
    print(f"{word_number(text)} words found in the document.")
    print(count_char(text))

if __name__ == "__main__":
    main()