# Written by Eric Martin for COMP9021


'''
Vigenere cipher:
- Encryption
- Decryption
- Breaking key

Example for the key ABRACADABRA and the beginning of the text
"Alice's Adventures in Wonderland" by  Lewis Carroll (Charles Lutwidge Dodgson)
(writing ' for \', \ for \\, † for \t, and ® for \n):
0         1         2         3         4         5         6         7         8         9
0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ †®
ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ †®0123456789abcdefghijklmnopqrstuvwxyz
BCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ †®0123456789abcdefghijklmnopqrstuvwxyzA
CDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ †®0123456789abcdefghijklmnopqrstuvwxyzAB
DEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ †®0123456789abcdefghijklmnopqrstuvwxyzABC
RSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ †®0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ

ABRACADABRA
Alice was b           +W*MQx*K$OL
eginning to           OR*XZS!Qy?Y
get very ti           xR&$z&R"*O$
red of sitt           S#&NzYSx$*$
ing by her            $T/QzL,xS&"
sister on t           x$*#&O%xZ/x
he bank, an           $S&xNK!UdOK
'''


from string import printable
from collections import defaultdict, Counter
from re import split
from operator import itemgetter, getitem
from functools import partial
from itertools import product


# From most frequent to least frequent letter in English
etaoin = {'etaoinshrdlcumwfgypbvkjxqz'[i]: i for i in range(26)}
# We eliminate from printable \r, \x0b (vertical tab) and \x0c (new page)
possible_keys = printable[: -3]
shifts = {possible_keys[i]: i for i in range(len(possible_keys))}
dictionary = None
# Default parameters for break_key() and break_key_for_file(),
# in which they can be changed as keyword only arguments.
nb_of_options_for_subkey = 2
max_key_length = 16
fraction_of_letters = .7
fraction_of_words = .5
etaoin_length = 6


def encrypt_file(key, filename, encrypted_filename = None):
    try:
        with open(filename) as file:
            if encrypted_filename:
                try:
                    with open(encrypted_filename, 'x') as encrypted_file:
                        print(encrypt(key, file.read()), end = '', file = encrypted_file)
                except FileExistsError:
                    print(f'{encrypted_filename} already exists, giving up.')                    
            else:
                return encrypt(key, file.read())
    except FileNotFoundError:
        print(f'Could not open {filename}, giving up.')

def decrypt_file(key, filename, decrypted_filename = None):
    try:
        with open(filename) as file:
            if decrypted_filename:
                try:
                    with open(decrypted_filename, 'x') as decrypted_file:
                        print(decrypt(key, file.read()), file = decrypted_file)
                except FileExistsError:
                    print(f'{decrypted_filename} already exists, giving up.')
            else:
                return decrypt(key, file.read())
    except FileNotFoundError:
        print(f'Could not open {filename}, giving up.')

def break_key_for_file(filename, *, nb_of_options_for_subkey = nb_of_options_for_subkey,
                         max_key_length = max_key_length, fraction_of_letters = fraction_of_letters,
                                fraction_of_words = fraction_of_words, etaoin_length = etaoin_length
                      ):
    try:
        with open(filename) as file:
            break_key(file.read(), nb_of_options_for_subkey = nb_of_options_for_subkey,
                         max_key_length = max_key_length, fraction_of_letters = fraction_of_letters,
                                fraction_of_words = fraction_of_words, etaoin_length = etaoin_length
                     )
    except FileNotFoundError:
        print(f'Could not open {filename}, giving up.')

def encrypt(key, text):
    return encrypt_or_decrypt(key, text, 1)

def decrypt(key, text):
    return encrypt_or_decrypt(key, text, -1)

def encrypt_or_decrypt(key, text, mode):
    return ''.join(possible_keys[(shifts[text[i]] + shifts[key[i % len(key)]] * mode) % len(shifts)]
                                                                           for i in range(len(text))
                  )

def break_key(text, *, nb_of_options_for_subkey = nb_of_options_for_subkey,
                         max_key_length = max_key_length, fraction_of_letters = fraction_of_letters,
                                fraction_of_words = fraction_of_words, etaoin_length = etaoin_length
             ):
    global dictionary
    if not dictionary:
        dictionary_filename = 'dictionary.txt'        
        try:
            with open(dictionary_filename) as file:
                dictionary = {w.strip().lower() for w in file}
        except FileNotFoundError:
            print(f'Could not open the dictionary file {dictionary_filename}, giving up.')
            return
    relevant_factors = []
    # Kasiski examination
    # Collecting all factors between 2 and max_key_length of the distances between
    # the starts of two consecutive occurrences of a string of length between 3 and 5. 
    for n in range(3, 6):
        for i in range(len(text) - 2 * n):
            n_gram = text[i: i + n]
            j = text.find(n_gram, i + n)
            if j != -1:
                relevant_factors.extend(factors(j - i, max_key_length))
    # The length of the key is likely to be one of the most frequent factors.
    # Also, as 1 is the first element of key_lengths, the Caesar cipher will be tried first.
    key_lengths = [1] + factors_from_most_to_least_frequent(relevant_factors)
    # Still, keys of any length at most equal to max_key_length will be tried if needed.
    key_lengths.extend(i for i in range(2, max_key_length + 1) if i not in key_lengths)
    for key_length in key_lengths:
        # Each subkey will be assigned one of the nb_of_options_for_subkey many characters
        # according to a frequency analysis of that part of the text it encodes
        # (more precisely, the n-th subkey encodes every key_length-th character in text,
        # starting with the n-th character).
        subkeys = []
        for n in range(key_length):
            scores = [(subkey, etaoin_score(decrypt(subkey, text[n: : key_length]), etaoin_length))
                                                                         for subkey in possible_keys
                     ]
            scores.sort(key = itemgetter(1), reverse = True)
            subkeys.append(x[0] for x in scores[: nb_of_options_for_subkey])
        for key in (''.join(subkey) for subkey in product(*subkeys)):
            print(key)
            decrypted_text = decrypt(key, text)
            if looks_like_English(decrypted_text, fraction_of_letters, fraction_of_words):
                print('What about this?\n')
                print(decrypted_text[: 200], '...')
                print()
                print("Enter Y[es] if happy, otherwise press any key and I'll keep working.")
                yes_or_no = input('> ')
                if yes_or_no in {'YES', 'Yes', 'yes', 'Y', 'y'}:
                    print(f'The key is: "{key}"')
                    return
    print('Sorry, I did my best...')

def factors(num, max_key_length):
    '''
    >>> tuple(factors(2, 10))
    (2,)
    >>> tuple(factors(4, 10))
    (2, 4)
    >>> tuple(factors(100, 10))
    (2, 4, 5, 10)
    '''
    return (i for i in range(2, max_key_length + 1) if num % i == 0)

def factors_from_most_to_least_frequent(factors):
    '''
    >>> factors_from_most_to_least_frequent((2, 4, 5, 10, 2, 4, 2)) in ([2, 4, 10, 5],\
                                                                                      [2, 4, 5, 10]\
                                                                       )
    True
    '''
    return [x[0] for x in sorted(Counter(factors).items(), key = itemgetter(1), reverse = True)]

def etaoin_score(text, length):
    '''
    # In 'Three masts' we have, in a case insensitive manner and
    # w.r.t. the reverse order of the letters in 'etaoinshrdlcumwfgypbvkjxqz':
    #   - 's', 't' and 'e', occuring twice
    #   - 'm', 'r', 'h' and 'a', occurring once.
    >>> etaoin_score('Three masts', 1) #  's'        'e'
    0
    >>> etaoin_score('Three masts', 2) #  'st'       'et'
    1
    >>> etaoin_score('Three masts', 3) #  'ste'      'eta'
    2
    >>> etaoin_score('Three masts', 4) #  'stem'     'etao'
    2
    >>> etaoin_score('Three masts', 5) #  'stemr'    'etaoi'
    2
    >>> etaoin_score('Three masts', 6) #  'stemrh'   'etaoin'
    2
    >>> etaoin_score('Three masts', 7) #  'stemrha'  'etaoins'
    4
    >>> etaoin_score('Three masts', 8) #  'stemrha'  'etaoinsh'
    5
    >>> etaoin_score('Three masts', 9) #  'stemrha'  'etaoinshr'
    6
    >>> etaoin_score('Three masts', 10) # 'stemrha'  'etaoinshrd'
    6
    '''
    letter_counts = Counter(c.lower() for c in text if c.isalpha())
    letters_for_given_counts = defaultdict(list)
    for c in letter_counts:
        letters_for_given_counts[letter_counts[c]].append(c)
    top_letters = (letter for count in sorted(letters_for_given_counts, reverse = True)
                                        for letter in sorted(letters_for_given_counts[count],
                                                      key = partial(getitem, etaoin), reverse = True
                                                            )
                  )
    return sum(1 for _ in range(length) if etaoin[next(top_letters)] < length)

def looks_like_English(text, fraction_of_letters, fraction_of_words):
    if sum(1 for c in text if c.isalpha()) / len(text) < fraction_of_letters:
        return False
    possible_words = split('[^a-zA-Z]+', text)
    nb_of_words = sum(1 for w in possible_words if w in dictionary)
    return nb_of_words / len(possible_words) > fraction_of_words


if __name__ == '__main__': 
    import doctest
    doctest.testmod()    
