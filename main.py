def read_book(file_name):
    file_content = ""    
    with open(file_name) as f:
        file_content = f.read()

    print(f"--- Begin report of {file_name} ---")
    
    words = word_count(file_content)
    print(f"{words} words found in the document")
    print()

    letters = letter_count(file_content)
    sorted_letters = sorted([(k, v) for k, v in letters.items()], key=lambda e: e[1], reverse=True)
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")
                

def word_count(text):    
    words = text.split()    
    return len(words)

def letter_count(text):
    counter = dict()
    for word in text.split():
        for letter in word.lower():
            if not letter.isalpha():
                continue
            counter[letter] = counter.get(letter, 0) + 1
    return counter

if __name__ == '__main__':
    read_book('books/frankenstein.txt')