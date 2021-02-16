class InvalidNationalId(Exception):
    def __init__(self, national_id):
        self.card_number = national_id
        self.message = national_id + ' is an invalid national id'
        super().__init__(self.message)
