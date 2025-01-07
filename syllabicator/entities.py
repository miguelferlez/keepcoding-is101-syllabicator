from syllabicator.funcs import split_phrase, intercalate, deintercalate

class Syllabicator():
    def __init__(self, phrase:str):
        self.phrase = phrase
        self.words = split_phrase(phrase)
    
    def intercalate(self, inter_syllable:str)->str:
        result = intercalate(self.phrase, inter_syllable)
        return result

    def deintercalate(self, inter_syllable:str)->str:
        result = deintercalate(self.phrase, inter_syllable)
        return result
    
    def __eq__(self, other:object)->bool:
        if isinstance(other, str):
            return self.words == other
        elif isinstance(other, self.__class__):
            return self.words == other.words
        return False

    def __str__(self):
        return self.words
    
    def __repr__(self):
        return self.__str__()



