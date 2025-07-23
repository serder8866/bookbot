def word_number(text: str) -> int:
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_char(text: str) -> dict:
    """
    Takes text as input an return a dictionary in the for character: count.
    
    Args:
        text (str): The text to count the characters in.
        
    Returns:
        dict: Character: Count pairs.
    """
    lowercase = text.lower()
    dic = {}
    for char in lowercase:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

if __name__ == "__main__":
    main()