from tire.tire import tire

class Octoprime(tire):

    def __init__(self, tireArray):
        self.tireArray = tireArray

    def needs_service(self):
        total = 0
        for i in self.tireArray:
            total += i

        if total >= 3:
            return True
        else:
            return False