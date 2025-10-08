def get_num_words(book_content):
    words = book_content.split()
    return len(words)
def character_count(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():  # only count letters
            counts[char] = counts.get(char, 0) + 1
    return counts

def sort_on(item):
    return item["num"]

def sort_count(char_dict):
    sorted_list = []
    for char, num in char_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    


#def character_count(book_content):
    count = [
        {"char": "a", "num": 0},
        {"char": "b", "num": 0},
        {"char": "c", "num": 0},
        {"char": "d", "num": 0},
        {"char": "e", "num": 0},
        {"char": "f", "num": 0},
        {"char": "g", "num": 0},
        {"char": "h", "num": 0},
        {"char": "i", "num": 0},
        {"char": "j", "num": 0},
        {"char": "k", "num": 0},
        {"char": "l", "num": 0},
        {"char": "m", "num": 0},
        {"char": "n", "num": 0},
        {"char": "o", "num": 0},
        {"char": "p", "num": 0},
        {"char": "q", "num": 0},
        {"char": "r", "num": 0},
        {"char": "s", "num": 0},
        {"char": "t", "num": 0},
        {"char": "u", "num": 0},
        {"char": "v", "num": 0},
        {"char": "w", "num": 0},
        {"char": "x", "num": 0},
        {"char": "y", "num": 0},
        {"char": "z", "num": 0},
        {"char": " ", "num": 0},
        {"char": ",", "num": 0},
        {"char": ".", "num": 0},
        {"char": "!", "num": 0},
        {"char": "?", "num": 0}
    ]
    for charater in book_content:
        if charater.lower() in count:
            count[charater.lower()] += 1
            print(f"debug: {charater}")
    return count            
#def sort_count(count):
    for char in count:
        if char.isalpha():
            print(f"The '{char}' character was found {count[char]} times")
    return
#def sort_on(dict):
    return dict["num"]


