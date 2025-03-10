def get_num_words(str):
    word_list = str.split()
    return len(word_list)


def get_num_char(str):
    char_count = {}
    for char in str:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(dict):
    return dict["num"]

def create_list(dict):
    lst = []
    for char in dict:
        lst.append({"char": char, "num": dict[char]})
    lst.sort(reverse=True, key=sort_on)
    return lst
