CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
OPEN_VOWELS = ['a', 'e', 'o', 'á', 'é', 'ó', 'ú']
CLOSE_VOWELS = ['i', 'í', 'u', 'ü']
SEMIVOWEL = 'y'
CONSONANT_PAIRS = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'gl', 'gr', 'kl', 'kr', 'll', 'pl', 'pr', 'rr', 'tl', 'tr']

def is_diphthong(vowel:str, prev_vowel:str)->bool:
    is_diphthong = False

    if prev_vowel in CLOSE_VOWELS and vowel in CLOSE_VOWELS:
        is_diphthong = True
    elif prev_vowel in OPEN_VOWELS and vowel in CLOSE_VOWELS:
        is_diphthong = True
    elif prev_vowel in CLOSE_VOWELS and vowel in OPEN_VOWELS:
        is_diphthong = True

    return is_diphthong

def is_triphthong(vowel:str, prev_vowel:str, antprev_vowel:str)->bool:
    is_triphthong = False

    if antprev_vowel in CLOSE_VOWELS :
        if prev_vowel in OPEN_VOWELS:
            if vowel in CLOSE_VOWELS or vowel == 'y':
                is_triphthong = True

    return is_triphthong

def is_consonant_pair(char:str, prev_char:str)->bool:
    char_pair = prev_char + char

    return char_pair in CONSONANT_PAIRS

def split(word:str):
    VOWELS = OPEN_VOWELS + CLOSE_VOWELS
    result = []
    prev_char = ''
    vowel_pos = []
    current_pos = 0
    
    for index, char in enumerate(word.lower()):
        if char in VOWELS or char == 'y':
            if is_consonant_pair(prev_char, word[index-2]):
                vowel_pos.append(index-2)
            elif prev_char in CONSONANTS or prev_char == 'y':
                vowel_pos.append(index-1)
            elif is_triphthong(char, prev_char, word[index-2]):
                vowel_pos.pop(-1)
            elif is_diphthong(char, prev_char) or word[-1] == 'y':
                vowel_pos.append(index+1)
            else:
                vowel_pos.append(index)
        prev_char = char

    for pos in vowel_pos[1:]:
        result.append(word[current_pos:pos])
        current_pos = pos

    result.append(word[current_pos:len(word)])
    result = list(filter(None, result))

    print(result)
    return result

if __name__ == '__main__':
    split('inaccion')
    split('paraguay')
    split('cambiéis')
    split('miau')
    split('fluye')