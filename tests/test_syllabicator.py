from syllabicator.entities import Syllabicator
import pytest

def test_syllabicator_word():
    assert Syllabicator('constante') == 'cons tan te'

def test_syllabicator_phrase():
    assert Syllabicator('hola, mundo') == 'ho la, mun do'
