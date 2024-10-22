with open('books/frankenstein.txt','r') as file:
    content=file.read()

    def print_report(file_path):
        with open('books/frankenstein.txt', 'r') as file:
            content = file.read()

        total_words = count_words(content)


        chars_dict = get_chars_dict(content)


        sorted_chars = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)


        print(f"--- Begin report of {file_path} ---")
        print(f"{total_words} words found in the document\n")
    
        for char, count in sorted_chars:
            if char.isalpha():
                print(f"The '{char}' character was found {count} times")
    
        print("--- End report ---")
    


def count_words(content):
    words = content.split()
    return len(words)

def get_chars_dict(content):
    chars = {}
    for c in content:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

    
print_report('books/frankenstein.txt')








    

