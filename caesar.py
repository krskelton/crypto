from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    #create a new empty string
    return_string = ''
    #for loop to go through each character in the message
    for char in text:
        #check if the character is an alpha character
        if char.isalpha() == False:
            #if not, just add it to the string
            return_string += char
        else:
            #if it is an alpha character call the rotate_character function
            return_string += rotate_character(char, rot)
    #return the new string
    return return_string
