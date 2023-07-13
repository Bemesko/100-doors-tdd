class Door:
    is_open = False

    def __init__(self, is_open=False):
        self.is_open = is_open

    def toggle_open(self):
        self.is_open = not self.is_open

class DoorList:
    doors = []
    
    def __init__(self, doors: int):
        for i in range(doors):
            self.doors.append(Door(False))
            
    def list_open_doors(self):
        doors_list = map(lambda door : door.is_open, self.doors)
        return doors_list