from tire.tire import tire


class Carrigan(tire):

    def __init__(self, tireArray):
        self.tireArray = tireArray
    
    def needs_service(self):
        for i in self.tireArray:
            if i >= 0.9:
                return True
            
        return False