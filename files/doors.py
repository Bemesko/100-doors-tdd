class Door:
    is_open = False

    def __init__(self, is_open: bool):
        self.is_open = is_open

    def toggle_open(self):
        self.is_open = not self.is_open
