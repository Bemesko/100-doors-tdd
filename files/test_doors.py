from doors import Door, DoorList

def test_close_open_door():
    door = Door(is_open=True)
    door.toggle_open()
    assert door.is_open is False
    
def test_open_closed_door():
    door = Door(is_open=False)
    door.toggle_open()
    assert door.is_open is True
    
def test_create_default_door():
    door = Door()
    assert door.is_open is False
    
def test_create_list_of_doors():
    door_list = DoorList(doors=5)
    assert len(door_list.doors) == 5

def test_all_doors_are_false():
    door_list = DoorList(doors=3)
    open_doors = sum(door_list.list_open_doors())
    
    assert open_doors == 0
    
def test_toggle_all_doors_should_make_all_open():
    doorAmount = 3
    door_list = DoorList(doors=doorAmount)
    door_list.toggle_doors(step=1)
    open_doors = sum(door_list.list_open_doors())
    
    assert open_doors == doorAmount