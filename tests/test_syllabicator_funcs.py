from syllabicator.funcs import split

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
