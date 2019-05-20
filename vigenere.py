from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    #create a new empty string
    return_string = ''
    #get the length of the key
    length_of_key = len(key)
    #index for text characters that are not alpha characters
    non_alpha = 0

    #for loop to iterate through the text characters
    for idx, char in enumerate(text):
        #check if the character is an alpha character
        if char.isalpha() == False:
            #if not, just add it to the string
            return_string += char
            non_alpha += 1
        else:
            #set the rotation from the key's alphabet position
            rotation = alphabet_position(key[(idx - non_alpha) % length_of_key])
            #if it is an alpha character call the rotate_character function
            return_string += rotate_character(char, rotation)        
    #return the new string
    return return_string
