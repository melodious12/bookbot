def word_count(text):
    words = text.split()
    count = len(words)
    print(count)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count(file_contents)
main()