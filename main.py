def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    letters = []
    print(f"{num_words} words found in this text.")
    # add each letter to the list of letters occuring in the text
    for c in chars_dict:
        if c.isalpha():
            letters.append(c)
    # sort the letters alphabetically
    letters.sort()
    for l in letters:
        print(f"The '{l}' character was found {chars_dict[l]} times")



def get_book_text(path):
    with open(path) as f:
        return f.read()
        

def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()