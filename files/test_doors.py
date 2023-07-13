from doors import Door

def test_close_open_door():
    door = Door(is_open=True)
    door.toggle_open()
    assert door.is_open is False
    
def test_open_closed_door():
    door = Door(is_open=False)
    door.toggle_open()
    assert door.is_open is True
