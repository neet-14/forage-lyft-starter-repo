from battery.battery import Battery
from car import Car
from datetime import date

class Nubbin_battery(Battery,Car):
    
    def __init__(self,last_service_date,current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self)->[bool]:
        d = date(self.current_Date)-date(self.last_service_date)
        if d.years >= 4:
            return True
        else:
            return False