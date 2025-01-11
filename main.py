def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_summary(book_path, num_words, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    low_text = text.lower()
    chars = {}
    for s in low_text:
        if s in chars:
            chars[s] += 1
        else: 
            chars[s] = 1
    return chars

def print_summary(book, words, chars):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document\n")
    alpha_chars = {}
    for char in chars:
        if char.isalpha() == True:
            alpha_chars[char] = chars[char]
    sorted_alpha_chars = dict(sorted(alpha_chars.items()))
    for char in sorted_alpha_chars:
        print(f"The '{char}' character was found {sorted_alpha_chars[char]} times")
    print("--- End report ---")

main()