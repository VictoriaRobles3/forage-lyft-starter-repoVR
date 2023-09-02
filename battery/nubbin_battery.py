from battery.battery import Battery
from updateDate import addBatteryLife

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        batteryLife = 4

        nubbin_should_be_serviced = addBatteryLife(self.last_service_date, batteryLife)
        if nubbin_should_be_serviced < self.current_date:
            return True
        else:
            return False
