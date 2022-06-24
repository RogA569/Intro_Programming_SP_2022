def single_letter_decryption(letter, key):
    """
    Returns a letter that is shifted by a specified value.
    If the parameter letter is not an actual letter of the English alphabet, returns the parameter as itself.
    :param letter: str
    :param key: int
    :return: int
    """
    shifted_letter_value = ord(letter) - key # calculate the ordinal value of letter shifted by key value
    if ord(letter) > 64 and ord(letter) < 91: # applies to uppercase letters
        if shifted_letter_value < ord('A'): # applies to letters whose shifted value goes past 'A'
            dist_from_A = (ord('A')) - shifted_letter_value # calculate how far from 'A' the shifted letter is
            shifted_letter = chr(ord('Z') - dist_from_A + 1) # shift letter from 'Z'; add 1 to account for 'A' rollover
        else:
            shifted_letter = chr(shifted_letter_value) # default
    elif ord(letter) > 96 and ord(letter) < 123: # applies to lowercase letters
        if shifted_letter_value < ord('a'): # applies to letters whose shifted value goes past 'a'
            dist_from_a = (ord('a')) - shifted_letter_value # calculate how far from 'a' the shifted letter is
            shifted_letter = chr(ord('z') - dist_from_a + 1) # shift letter from 'z'; add 1 to account for rollover from 'a'
        else:
            shifted_letter = chr(shifted_letter_value) # default
    else:
        shifted_letter = letter # letter is not an actual letter, so the unshifted input is returned
    
    return shifted_letter

def decode_caesar(encoded_message, key):
    """
    Returns a decrypted message of the Caesar cipher kind.
    :param encoded_message: str
    :param key: int
    :return: str
    """
    decrypted_message = "" # initialize string that will contain the decrypted message
    for char in encoded_message: # go through each character in the encoded message
        decrypted_char = single_letter_decryption(char, key) # use the single_letter_decryption function to decrypt each character
        decrypted_message += decrypted_char # add decrypted character to the message
    
    return decrypted_message

def main():
    decryption_key = int(input("Enter the decryption key: ")) # user prompt for decryption key, which is saved in variable as an integer
    line = input("Enter the encoded line: ") # user prompt for encoded message; saved in variable
    decryption = decode_caesar(line, decryption_key) # decryption result saved in variable
    print(decryption) # print result

main()
