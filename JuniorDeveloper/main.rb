=begin
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
=end

def encode_railroad(secret_phrase)
    toggle      = true
    upper_track = []
    lower_track = []

    secret_phrase.split(" ").each do |word|
        if toggle
            upper_track << word
            toggle = false
        else
            lower_track << word
            toggle = true
        end
    end
    return "#{upper_track.join(" ")}\r\n#{lower_track.join(" ")}"
end

# fill out this method
def decode_railroad(encoded_phrase)
    # if hi my name is ryan becomes
    # hi name ryan
    # my is
    # how would you decode this?
end

def shuffle_letter(letter_to_shuffle, places_to_shuffle)
    # with places_to_shuffle = 1, a becomes b, b becomes c, etc.
    caesar_string = letter_to_shuffle
    letter_to_shuffle.scan (/./) do |char|
        # ruby regex to identify only letters
        if char.match(/^[[:alpha:]]$/) # Identify letters only.
            caesar_string = get_next_char(char, places_to_shuffle)
        end
    end
    return caesar_string
end

#fill out this method
def unshuffle_letter(letter_to_decode, places_to_unshuffle)
    # how would you reverse the shuffle_letter function?
end

# this is a helper method to shift letters forward by a set number of places
# you will probably need to implement something in reverse...
def get_next_char(char, places_to_go_forward)
    alpha       = "abcdefghijklmnopqrstuvwxyz"
    alpha_arr   = alpha.split('')
    index       = alpha_arr.find_index(char)

    places_to_go_forward.times do |iteration|
        index += 1
        if index > 25
            index = 0
        end
    end

    return alpha_arr[index]
end

def encode_secret_message(secret_message, seed)
    encoded_message = ""
    index = 0
    secret_message.split(" ").each do |word|
        caesar_seed = seed[index].to_i
        caesared_word = ""
        word.split("").each do |char|
            caesared_word += shuffle_letter(char, caesar_seed)
        end
        encoded_message += "#{caesared_word} "
        index += 1
    end
    return encode_railroad(encoded_message)
end

puts "Welcome to the Cloverhound Junior Software Developer test"
# do not edit either seed or secret message as it will prevent you from completing this assessment.
seed = '4578697581264578697781265583416'
secret_message = "gsrkvexypexmsrw! ohcl znoy wslhzl rwja@ktwdmzpwcvl.kwu aqwt jezsvmxi huk eua h wz rgtuqp. xzgojhy apwctl nv yurazout.\r\ndtz awtdml ydiiun. jrfnq xjui yurazout, mtggd, epmbpmz jan jha eph znk qnsj eh efwfmpqfs"
# this code below is optional and not necessary for your solution, but may give you some insight as to how
# the above message was encoded

# start optional code
message_to_be_encoded = '' # this message would have the same number of words as there are numbers in seed
encoded_message = encode_secret_message(message_to_be_encoded, seed)
puts encoded_message
#puts encoded_message
# end optional code
# use the space below to decode secret_message