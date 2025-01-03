from syllabicator.funcs import split

def test_split():
    assert split('elefante') == ['e', 'le', 'fan', 'te']
    assert split('constante') == ['cons', 'tan', 'te']
    assert split('inaccion') == ['in', 'ac', 'cion']
    
def test_split_diphthong():
    assert split('caucho') == ['cau', 'cho']
    assert split('agua') == ['a', 'gua']
    assert split('iones') == ['io', 'nes']

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
    
    assert split('fluye') == ['flu', 'ye']
