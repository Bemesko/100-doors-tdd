from christmas import to_ordinal, get_present, sing_verse

def test_should_convert_1_to_first():
    assert to_ordinal(1) == 'first'

def test_should_convert_12_to_twelfth():
    assert to_ordinal(12) == 'twelfth'
    
def test_should_convert_5_to_fitfh():
    assert to_ordinal(5) == 'fifth'
    
def test_should_return_first_present_for_1():
    assert get_present(1) == 'A partridge in a pear tree.'
    
def test_should_return_second_present_for_2():
    assert get_present(2) == 'Two turtle doves and'
    
def test_should_return_eleventh_present_for_11():
    assert get_present(11) == 'Eleven pipers piping'
    
def test_should_return_unknown_present_for_invalid_day():
    assert get_present(0) == 'Unknown present'
    
def test_should_return_first_verse_for_day_1():
    assert sing_verse(1) == 'On the first day of Christmas my true love gave to me: A partridge in a pear tree. '
    
def test_should_return_second_verse_for_day_2():
    assert sing_verse(2) == 'On the second day of Christmas my true love gave to me: Two turtle doves and A partridge in a pear tree. '
