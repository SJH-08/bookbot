def main(): 
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    nb_words = word_count(text)
    chars_dict = char_count(text)
    output = get_report(chars_dict, nb_words)
    print(output)


#word_count in the text file = 77986
#split str file --> count each word occurance --> int
def word_count(text):
    count1 = 0
    words = text.split()
    for f in words:
        count1 += 1
    return count1

#char_count in text file 
#create empty dict --> lowercase all chars
#if char already in dict --> +1
#otherwise: add +1
def char_count(text):
    chars = {}
    for c in text: 
        lowered_string = c.lower()
        if lowered_string in chars: 
            chars[lowered_string] += 1
        else: 
            chars[lowered_string] = 1
    return chars

#check that all chars are letters
#sort chars
#print report 
 
def sort_on(dict):
    return dict["count"]

def get_report(chars_dict, nb_words): 
    char_list = []
    
    # Build our list of dictionaries
    for char in chars_dict:
        if char.isalpha(): 
            new_dict = {
                "character": char,
                "count": chars_dict[char]
            }
            char_list.append(new_dict)
    
    # Sort using our sort_on function
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{nb_words} words found in the document")

    for char_dict in char_list:
        print(f"The '{char_dict['character']}' character was found {char_dict['count']} times")
    return "--- End report ---"


#open and read file 
def book_text(path):
    with open(path) as f:
        return f.read()

main()
