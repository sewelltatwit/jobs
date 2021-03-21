"""
    Welcome applicants!
    The point of this little test is to help us determine your skillset.
    On the job it will be very common that you are handed an unfamiliar codebase
    and instructed to debug and determine what is not functioning properly.
    Once you have fixed this properly, instructions will be printed to your terminal
    instructing you on what to do for your next steps.

    The two key concepts here are a caesar cipher and a railroad code

    Your goal is to decode the secret message below stored in secret_message

    Good luck!

    - Ryan

    P.S
    I hope you enjoy puzzles
"""

import random

def encode_railroad(secret_phrase):
    toggle      = True
    upper_track = []
    lower_track = []

    for word in secret_phrase.split(" "):
        if toggle:
            upper_track.append(word)
            toggle = False
            continue
        lower_track.append(word)
        toggle = True

    return "{}\r\n{}".format(" ".join(upper_track), " ".join(lower_track))

# fill out this method
def decode_railroad(encoded_phrase):
    # if hi my name is ryan becomes
    # hi name ryan
    # my is
    # how would you decode this?
    upper_track, lower_track = encoded_phrase.split("\r\n",1)
    upper=upper_track.split()
    lower=lower_track.split(" ")
    decoded_phrase = ""
    for x in range(len(upper)):
        decoded_phrase+=upper[x] + " "
        if len(lower)>x:
            decoded_phrase+= lower[x]+" "
    return decoded_phrase[:-1]

def shuffle_letter(letter_to_shuffle, places_to_shuffle):
    # with places_to_shuffle = 1, a becomes b, b becomes c, etc.
    if not letter_to_shuffle.isalpha():
        return letter_to_shuffle
    return chr((ord(letter_to_shuffle) + places_to_shuffle - 97) % 26 + 97)

#fill out this method
def unshuffle_letter(letter_to_decode, places_to_unshuffle):
    # how would you reverse the shuffle_letter function?
    if not letter_to_decode.isalpha():
        return letter_to_decode
    return chr((ord(letter_to_decode) - places_to_unshuffle - 97) % 26 + 97)

def encode_secret_message(secret_message, seed):
    encoded_message = ""
    index = 0
    for word in message_to_be_encoded.split(" "):
        caesar_seed = int(seed[index])
        caesared_word = ""
        for char in word:
            caesared_word += shuffle_letter(char, caesar_seed)
        encoded_message += "{} ".format(caesared_word)
        index += 1
    return encode_railroad(encoded_message)

if __name__ == '__main__':
    print("Welcome to the Cloverhound Junior Software Developer test")
    # do not edit either seed or secret message as it will prevent you from completing this assessment.
    seed = '4578697581264578697781265583416'
    secret_message = "gsrkvexypexmsrw! ohcl znoy wslhzl rwja@ktwdmzpwcvl.kwu aqwt jezsvmxi huk eua h wz rgtuqp. xzgojhy apwctl nv yurazout.\r\ndtz awtdml ydiiun. jrfnq xjui yurazout, mtggd, epmbpmz jan jha eph znk qnsj eh efwfmpqfs"
    # this code below is optional and not necessary for your solution, but may give you some insight as to how
    # the above message was encoded
    
    # start optional code
    message_to_be_encoded = 'one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twentyone twentytwo twentythree twentyfour twentyfive twentysix twentyseven twentyeight twentynine thirty thirtyone' # this message would have the same number of words as there are numbers in seed
    encoded_message = encode_secret_message(message_to_be_encoded, seed)
    # end optional code
    # use the space below to decode secret_message
    message=decode_railroad(secret_message)
    
    decoded_message = ""
    i= 0
    for word in message.split(" ")[:-1]:
        _seed = int(seed[i])
        _word = ""
        for char in word:
            _word += unshuffle_letter(char, _seed)
            
        decoded_message += "{} ".format(_word)
        i += 1
    print(decoded_message)
    