
def get_char_count(para):
    """This function accepts a string (str) and returns total no of string char (int)"""
    return len(para)


def get_word_count(para):
    return len(para.split(' '))


# punctaution count
def get_punctuation_count(text):
    punc = ['!', '@', '?', '.', '...', ',', ';', ':', '[', ']', "'", '"', '(', ')', '/', '-', '*', '{', '}' ]
    exception = ['[', '(', '{', '"']
    count = 0
    for x in punc:
        if x in text:
            count += text.count(x)
    return count


# puncatioin remove    
def remove_punctuation(text=''):
    punc = ['!', '@', '?', '.', '...', ',', ';', ':', '[', ']', "'", '"', '(', ')', '/', '-', '*', '{', '}' ]
    for x in punc:
        if x in text:
            text = text.replace(x, '')
    return text 
    

# addtion space remove
def additon_space_remove(text):
    return text.strip()
    


# find vowel
def get_vowels_count(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for x in vowels:
        if x in text:
            count += text.count(x)
    return count


    
    
    
