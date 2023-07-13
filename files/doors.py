class Door:
    is_open = false
    
    def __init__(self: Door, is_open: bool):
        self.is_open = is_open
        
    def toggle_open(self: Door):
        self.is_open = not self.is_open