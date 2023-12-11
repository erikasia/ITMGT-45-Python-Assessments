'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if letter == ' ':
        return (' ')
    else:

        list_loc = alphabet.index(letter)

        initial_loc = list_loc + shift
        loc = 0

        if initial_loc < 25:
            loc = initial_loc
            return (alphabet[loc])
        elif list_loc == 0:
            loc = initial_loc + 1
            return (alphabet[loc])
        else:
            loc = initial_loc - 26
            return (alphabet[loc])

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    shifted_message = ''

    for x in message:
        if x != ' ':
            list_loc = alphabet.index(x)
            letter_shift = list_loc + shift
            shifted_message = shifted_message + alphabet[letter_shift]
        else:
            shifted_message = shifted_message + ' '

    return str(shifted_message)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if letter == ' ':
        return (' ')
    else:

        num1 = alphabet.index(letter)
        num2 = alphabet.index(letter_shift)

        initial_loc = num1 + num2 
        loc = 0

        if initial_loc < 25:
            loc = initial_loc
            return (alphabet[loc])
        elif initial_loc == 0:
            loc = initial_loc + 1
            return (alphabet[loc])
        else:
            loc = initial_loc - 26
            return (alphabet[loc])

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    v_cipher = ''
    message_list = list(message)
    key_list = list(key)
    y = 0

    for x in message_list:
        if x == ' ':
            v_cipher = v_cipher + ' '
            y = y + 1
        else: 
            if y < len(key_list):
                v_cipher = v_cipher + key_list[y]
                y = y + 1
            else:
                y = 0
                v_cipher = v_cipher + key_list[y]
                y = y + 1

    half_cipher = v_cipher
    list_half_cipher = list(half_cipher)

    full_cipher = ''
    key_counter = 0

    for x in message:
        if x == ' ':
            full_cipher += ' '
            key_counter += 1
        else:
            if key_counter <= len(list_half_cipher):
                loc_a = alphabet.index(x)
                loc_b = alphabet.index(list_half_cipher[key_counter])
                loc = loc_a + loc_b
                if loc > 25:
                    loc -= 26
                    full_cipher += alphabet[loc]
                    key_counter += 1
                else:    
                    full_cipher += alphabet[loc]
                    key_counter += 1
            else:
                key_counter = 0
                loc_a = alphabet.index(x)
                loc_b = alphabet.index(list_half_cipher[key_counter])
                loc = loc_a + loc_b
                if loc > 25:
                    loc -= 26
                    full_cipher += alphabet[loc]
                    key_counter += 1
                else:
                    full_cipher += alphabet[loc]
                    key_counter += 1

    return str(full_cipher)