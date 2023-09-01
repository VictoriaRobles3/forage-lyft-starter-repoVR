from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_serice_date = last_service_date

    def needs_service(self):
        batteryLife = 2
        date_should_be_serviced = self.last_service_date + batteryLife
        if date_should_be_serviced < self.current_date:
            return True
        else:
            return False
