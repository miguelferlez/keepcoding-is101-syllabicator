CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
OPEN_VOWELS = ['a', 'e', 'o', 'á', 'é', 'ó', 'ú']
SEMIVOWEL = ['y']
CLOSE_VOWELS = ['i', 'í', 'u', 'ü']
CONSONANT_PAIRS = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'gl', 'gr', 'kl', 'kr', 'll', 'pl', 'pr', 'rr', 'tl', 'tr']

def is_word(word:str)->bool:
    ALPHABET = CONSONANTS + SEMIVOWEL + OPEN_VOWELS + CLOSE_VOWELS
    is_word = True
    for char in word.lower():
        if char not in ALPHABET:
            raise ValueError(f"cannot split word in syllables, '{word}' contains invalid characters")
    return is_word

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

def split(word:str)->list[str]:
    VOWELS = OPEN_VOWELS + CLOSE_VOWELS
    syllables = []
    vowel_pos = []
    prev_char = ''
    was_triphthong = False
    was_diphthong = False
    was_prefix = False
    current_pos = 0

    for index, char in enumerate(word.lower()):
        if char in VOWELS or char == 'y':
            if is_consonant_pair(prev_char, word[index-2]):
                vowel_pos.append(index-2)
            elif (prev_char in CONSONANTS or prev_char == 'y') and not was_prefix:
                vowel_pos.append(index-1)
            elif is_triphthong(char, prev_char, word[index-2]):
                was_diphthong = False
                was_triphthong = True
                vowel_pos.pop(-1)
            elif is_diphthong(char, prev_char) or word[-1] == 'y':
                was_diphthong = True
                vowel_pos.append(index+1)
            else:
                vowel_pos.append(index)
                was_prefix = False
        else:
            if char == 'n' or char == 's':
                if index == len(word)-1 and not was_triphthong:
                    vowel_pos.pop(-1)
                elif index == 1 and prev_char == 'i':
                    was_prefix = True
                    vowel_pos.append(index+1)
                elif index != 2 and was_diphthong:
                    vowel_pos.pop(-1)
            was_triphthong = False
            was_diphthong = False    
        prev_char = char

    for pos in vowel_pos[1:]:
        syllables.append(word[current_pos:pos])
        current_pos = pos

    syllables.append(word[current_pos:len(word)])
    syllables = list(filter(None, syllables))
    # result = ' '.join(syllables)

    return syllables

def split_phrase(phrase:str)->str:
    result = ''
    words = phrase.split()
    for word in words:
        syllable = ' '.join(split(word))
        result += syllable + ' '
    print(result.strip())
    return result.strip()

if __name__ == '__main__':
    split('inaccion')
    split('paraguay')
    split('cambiéis')
    split('miau')
    split('fluye')
    split('cienpies')
    split('yegua')
    split('anfibio')
    split('untado')

    split_phrase('hola, mundo!')