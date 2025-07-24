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

def sort_dict(dictionary: dict) -> list:
    """
    Turns a dictionary into a sorted list of dictionaries, sorted by the values of the initial dictionary.
    
    Args: A dictionary.
    
    Returns: A sorted list of dictionaries each with 2 key-value pairs.
    """
    separate_pairs = []
    for key in dictionary:
        key_val = {}
        if key.isalpha():
            key_val["character"] = key
            key_val["count"] = dictionary[key]
            separate_pairs.append(key_val)
        else:
            pass 
    separate_pairs.sort(reverse=True, key=lambda item: item["count"])
    return separate_pairs

if __name__ == "__main__":
    main()