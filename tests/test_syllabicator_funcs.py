from syllabicator.funcs import is_word, split, split_phrase, intercalate
import pytest

def test_split():
    assert split('elefante') == ['e', 'le', 'fan', 'te']
    assert split('constante') == ['cons', 'tan', 'te']
    assert split('inaccion') == ['in', 'ac', 'cion']
    assert split('alfabeto') == ['al', 'fa', 'be', 'to']
    
def test_split_diphthong():
    assert split('caucho') == ['cau', 'cho']
    assert split('agua') == ['a', 'gua']
    assert split('iones') == ['io', 'nes']
    assert split('cienpies') == ['cien',  'pies']
    assert split('anfibio') == ['an', 'fi', 'bio']

    assert split('soy') == ['soy']
    assert split('yegua') == ['ye', 'gua']

def test_split_triphthong():
    assert split('paraguay') == ['pa', 'ra', 'guay']
    assert split('cambiéis') == ['cam', 'biéis']
    assert split('miau') == ['miau']

def test_split_consonant_pairs():
    assert split('carretera') == ['ca', 'rre', 'te', 'ra']
    assert split('guerra') == ['gue', 'rra']
    assert split('chanchullo') == ['chan', 'chu', 'llo']
    
    assert split('imposible') == ['im', 'po', 'si', 'ble']
    assert split('imperfecto') == ['im', 'per', 'fec', 'to']
    assert split('fluye') == ['flu', 'ye']

def test_valid_word():
    assert is_word('constante') == True
    assert is_word('Inacción') == True
    assert is_word('CAUCHO') == True

    with pytest.raises(ValueError):
        is_word('R2D2')
    with pytest.raises(ValueError):
        is_word('has visto')
    with pytest.raises(ValueError):
        is_word('hola!')
    with pytest.raises(ValueError):
        is_word('Hola, mundo!')

def test_split_phrase():
    assert split_phrase('Hola, mundo!') == 'Ho la, mun do!'
    assert split_phrase('¿quieres un vaso de agua?') == '¿qui e res un va so de a gua ?'
    assert split_phrase('HAS VISTO') == 'HAS VIS TO'

def test_intercalate():
    assert intercalate('hola, me llamo ramón!', 'pi') == 'pihopila, pime pillapimo pirapimón!'