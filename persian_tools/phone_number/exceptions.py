class InvalidPhoneNumber(Exception):
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.message = phone_number + ' is an invalid phone number'
        super().__init__(self.message)


class InvalidToken(Exception):
    def __init__(self, token):
        self.token = token
        self.message = token + ' is an invalid token'
        super().__init__(self.message)
