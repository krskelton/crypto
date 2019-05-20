#define alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter): 
    #get the index of the current letter 
    return alphabet.index(letter.lower())

def rotate_character(char, rot):
    is_upper = ''
    #check to see if char is uppercase
    if char.isupper() == True:
        #if true, make lower
        is_upper = char.lower()
        #get position index and add rot
        new_index = ((alphabet_position(is_upper) + rot) % 26)
        #get new letter at this position
        return alphabet[new_index].upper()
    elif char.isalpha() == False:
        return 
    else:
        #get position index and add rot
        new_index = ((alphabet_position(char) + rot) % 26)
        #get new letter at this position
        return alphabet[new_index]
