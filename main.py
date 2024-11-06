def word_count(text):
    words = text.split()
    count = len(words)
    return count

def character_count(text):
    char_dict = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_count(file_contents)
        chars_dict = character_count(file_contents)
        print(chars_dict)
main()