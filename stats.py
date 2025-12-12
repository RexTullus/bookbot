def word_count(the_text):
    words=the_text.split()
    return len(words)

def char_count(the_text):
    chars={}
    for letter in the_text:
        count=0
        letter = letter.lower()
        if letter in chars:
            count = chars[letter]
            chars[letter] = count + 1
        else:
            chars[letter] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_dict(the_dict):
    sortlist=[]
    for item in the_dict:
        sortlist.append({"char":item,"num":the_dict[item]})
    sortlist.sort(reverse=True,key=sort_on)
    return sortlist

