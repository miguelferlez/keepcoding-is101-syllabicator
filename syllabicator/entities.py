from syllabicator.funcs import is_word, split, split_phrase

# class Syllabicator():
#     def __init__(self, words:str):
#         if len(words.split()) == 1:
#             if False in [is_word(word) for word in words.split()]:
#                 raise ValueError(f"cannot split word in syllables, '{words}' contains invalid characters")
#             else:
#                 self.value = split(words)
#         else:
#             self.value = split_phrase(words)

#     def __str__(self):
#         if type(self.value) == list:
#             result = ' '.join(self.value)
#         else:
#             result = self.value
#         return result
    
#     def __repr__(self):
#         return self.__str__()

#     def __eq__(self, other:object):
#         if isinstance(other, str):
#             return self.value == other
#         return False

class Syllabicator():
    def __init__(self, words):
        self.words = self.syllabify(words)

    def syllabify(self, words):
        result = split_phrase(words)
        return result

    def __eq__(self, otro):
        if isinstance(otro, str):
            return self.words == otro
        return False

    def __str__(self):
        return self.words
    
    def __repr__(self):
        return self.__str__()



