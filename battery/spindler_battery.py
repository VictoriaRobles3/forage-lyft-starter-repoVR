from battery.battery import Battery
from updateDate import addBatteryLife

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        batteryLife = 3
        spindler_should_be_serviced = addBatteryLife(self.last_service_date, batteryLife)
       ## service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + batteryLife)
        if spindler_should_be_serviced < self.current_date:
            return True
        else:
            return False
