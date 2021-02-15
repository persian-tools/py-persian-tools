class InvalidCardNumber(Exception):
    def __init__(self, card_number):
        self.card_number = card_number
        self.message = card_number + ' is an invalid card number'
        super().__init__(self.message)
