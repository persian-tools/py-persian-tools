class InvalidPlateLength(Exception):
    def __init__(self, plate):
        self.card_number = plate
        self.message = plate + ' digits long, must be 7 or 8'
        super().__init__(self.message)
