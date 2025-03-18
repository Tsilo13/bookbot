def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def count_characters(file_contents):
    character_counts = {}
    for char in file_contents:
        char = char.lower()
        if char not in character_counts:
            character_counts[char] = 1
        else:
            character_counts[char] += 1
    return character_counts

def sort_character_list(character_counts):
    sorted_list = []
    for char in character_counts:
        tiny_dict ={"character": char, "count": character_counts[char]}
        sorted_list.append(tiny_dict)
    sorted_list.sort(reverse=True, key= lambda tiny_dict: tiny_dict["count"])
    return sorted_list

