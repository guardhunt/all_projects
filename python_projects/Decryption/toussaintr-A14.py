######################################################################
#
# username: toussaintr -- Roland Junior Toussaint
#
# Assignment: A14
# Purpose: To practice importing files, working with strings and lists, then
# exporting and writing files through Python. Also allowed more practice with
# encapsulation.
#######################################################################
# Acknowledgements:
# Functions get_file_to_string & write_string_to_file written by Dr. Jan Pearce &
# Dr. Mario Nakazawa
#
# Files imported from http://cs.berea.edu/courses/csc226/tasks/cryptogram.txt, &
# http://cs.berea.edu/courses/csc226/tasks/orig_dist.txt
#################################################################################
# Functions
def get_file_to_string(input_str):
    ''' Opens a file by the name of input_str (eg. "crytogram.txt") and reads the contents
	one line at a time, appending what it read to source_text as it goes along.
	It ends when it reaches the end of the file and returns the contents
	in the string source_text.'''
    source_text = ""
    open_file = open(input_str, "r")
    next_line = open_file.readline()
    # This next loop makes sure to keep reading as long as what we read
    # in (stored in the variable next_line) is not blank.
    while(len(next_line) > 0):
        source_text = source_text + next_line
        next_line = open_file.readline()
    # we are done reading, so close the file and output success.
    open_file.close()
    # print (input_str + ' read.')
    return source_text

def create_list(input_string):
    '''This takes a string and breaks it into elements in a list. Returns the
    list of numbers'''
    list_o_num = []
    little_string = ''
    for i in input_string: # This steps through the string
        if i != ' ': # If it is not a space
            little_string += i # Add i to little_string
        elif i == ' ': # When it is a space
            list_o_num.append(int(little_string)) # Add the string made above to the new list
            little_string = "" # Clears the string
    list_o_num.append(int(little_string)) # Adds the last string at end of original string
    return list_o_num

def generate_frequency(input_string):
    '''This takes a string and creates a list with the number of times the 26
    letters in the alphabet occur in it. It returns it in a list made up of ints
    as elements based on [A, B, C ] being [0, 90, 24 ]'''
    count = 0
    new_list = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in alphabet: # Steps through 26 letter in alphabet
        for x in (input_string): # Steps through letters in input string
            if x == i: # if letter in alphabet = letter in input string add one to count
                count += 1
        new_list.append(count)  # Adds the letters count to the new list
        count = 0 # Resets count after each run
    return new_list

def decryption_key(coded_freq, uncoded_freq):
    '''This takes two parameters of the of the coded messages frequency and the
    uncoded messages frequency. It then compares the two frequencies and returns
    a new list with the code key. The list will corespond with [ a, b, c ]'''
    decryption_key = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in coded_freq:    # This steps through the coded freq list
        for x in range(len(uncoded_freq)): # This steps through the uncoded freq as int
            if i == uncoded_freq[x]: # If element in coded freq = element in uncoded
                decryption_key.append(alphabet[x]) # Insert coresponding letter from alphabet in new list
                del alphabet[x] # Delete letter from alphabet list so it cant be used again
                del uncoded_freq[x] # Delete letter from alphabet list so it cant be used again
                break # breaks for loop

    return decryption_key

def decode_encrypted(code_file, decryt_key):
    '''This takes the file that needs to be decoded and the decryption key that is in the
    form of a list. It steps through coded message and compares each letter individually
    to the decryption key, then it takes the index location of the letter in key and puts
    the letter from the letter from the alphabet with the same index value. It also watches
    missing spaces after '.' and makes letters that occur after '.' capitol letters. Returns
    the decrypted message'''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 0   # This is the index count for the coded message
    upper_count = 0 # This determines the state if the letter should be capital
    puncuation = [',', '!', '-', ' ', '\n']
    unencrypted = ''    # New String
    for i in code_file:   # Steps through coded file letters i == str
        if code_file[count] == '.':   # If the i is a period
            unencrypted += i    # It adds the . to the new string
            upper_count = 1 # Sets the state to upper count state to 1
            if code_file[count + 1 : count + 2] != ' ': # if letter after . not a space input a space into new string
                        unencrypted += ' '
        elif code_file[count] != '.': # If i not a .
            for x in range(len(alphabet)):  # Run through 0-25
                if i == alphabet[x]:    # if i equals letter in alphabet
                    if upper_count == 0:    # Looks at upper case state
                        if count == 0:  # Detects if it is first letter in string
                            unencrypted += decryt_key[x].upper()
                        else:   # Not first letter in string
                            unencrypted += decryt_key[x]
                    elif upper_count == 1:  # Checks state
                        unencrypted += decryt_key[x].upper() # Makes new letter upper case
                        upper_count = 0 # Resets state
                elif i in puncuation:   # Checks if i not in alphabet bu in puncuation
                    unencrypted += i
                    break # Ends the alphabet loop
        count += 1
    return unencrypted

def write_string_to_file(output_str):
    '''Open the output file "output.txt" and write the contents of
    output_str into it before closing the file'''
    open_file = file('toussaintr-decrypt.txt', "w") # ('File name', 'w' for write)
    open_file.write(output_str)
    print (output_str + '\ntoussaintr-decrypt.txt' + ' closed.') # Prints the return string
    open_file.close()

##################################################################################################
# This is the import for the coded file
crypto_file = get_file_to_string("cryptogram.txt")

# This imports the file of  original frequency
orig_frequency = get_file_to_string("orig_dist.txt")

# This counts the crypted messages frequency
crypto_frequency = generate_frequency(crypto_file)

# This creates the decrytion key to decode the doc
decryption_key = decryption_key(crypto_frequency, create_list(orig_frequency))

# This decryptes the document and writes it into the file with this code
write_string_to_file(decode_encrypted(crypto_file, decryption_key))






