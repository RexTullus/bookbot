from stats import word_count, char_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
  
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book_path=sys.argv[1]

    chars={}
    sorted_list={}
    book_text = get_book_text(book_path)
    num_words=word_count(book_text)
    chars=char_count(book_text)
    #print(f"Char Dict: {chars}")
    sorted_list=sort_dict(chars)
    #print("-------------------------")
    #print(f"Sorted List:  {sorted_list}")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    return sys.exit(0)

main()
