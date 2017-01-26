def alphabet_position(letter):          ### gets the ascii value of a letter
    z  = ord(letter)
    return z

def rotate_character(char, rot):        ### rotates letters according to a number set by the code
    y = alphabet_position(char)
    if y >= 65 and y <= 90:
        return chr(((y-65+rot)%26)+65)
    elif y >= 97 and y <= 122:
        return chr(((y-97+rot)%26)+97)
    else:
        return chr(y)

def encrypt(text, rot):
    newtext = ''
    for char in range(len(text)):
        newtext = newtext + rotate_character(text[char], rot)
    return newtext
