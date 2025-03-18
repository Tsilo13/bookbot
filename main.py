import sys
from stats import count_words, get_book_text, count_characters, sort_character_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    # print_text = get_book_text("books/frankenstein.txt")
    # print(print_text)
    word_count = count_words(get_book_text(path))
    character_count = count_characters(get_book_text(path))
    final_list = sort_character_list(character_count)
    # print(f"{word_count} words found in the document")
    # print(f"{character_count}")
    # print(f"{final_list}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------") 
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in final_list:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


if __name__ == "__main__":
    main()

