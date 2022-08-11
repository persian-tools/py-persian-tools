class InvalidEconomicNationalId(Exception):
    def __init__(self, economic_national_id):
        self.card_number = economic_national_id
        self.message = economic_national_id + ' is an invalid economic national id.'
        super().__init__(self.message)
