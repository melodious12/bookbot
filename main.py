def word_count(text):
    words = text.split()
    count = len(words)
    return count

def character_count(text):
    char_dict = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character.isalpha():
            if character in char_dict:
                char_dict[character] += 1
            else:
                char_dict[character] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def dict_to_sortable_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_amount_pair = {"char": char, "num": count}
        char_list.append(char_amount_pair)
    return char_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_count(file_contents)
        chars_dict = character_count(file_contents)
        lists = dict_to_sortable_list(chars_dict)
        lists.sort(reverse=True, key=sort_on)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        for char_dict in lists:
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
        print("--- End report ---")
main()