from syllabicator.entities import Syllabicator
import pytest

def test_syllabicator_word():
    assert Syllabicator('constante') == 'cons tan te'

def test_syllabicator_phrase():
    assert Syllabicator('hola, mundo') == 'ho la, mun do'

def test_syllabicator_intercalate():
    assert Syllabicator('constante').intercalate('pi') == 'piconspitanpite'
    assert Syllabicator('hola, mundo').intercalate('pi') == 'pihopila, pimunpido'

def test_syllabicator_deintercalate():
    assert Syllabicator('piconspitanpite').deintercalate('pi') == 'constante'
    assert Syllabicator('pihopila, pimunpido').deintercalate('pi') == 'hola, mundo'