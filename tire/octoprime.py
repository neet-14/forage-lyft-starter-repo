from tire.tire import tire

class Octoprime(tire):

    def __init__(self, tireArray):
        self.tireArray = tireArray

    def needs_service(self):
        return sum(self.tireArray) >= 3