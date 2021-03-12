class NotEnoughArguments(Exception):
    def __init__(self):
        self.message = 'Arguments are not enough; we need `bill_id` and `payment_id` or at least, bill `barcode`'
        super().__init__(self.message)
