from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        batteryLife = 4
        date_should_be_serviced = self.last_service_date + batteryLife
        if date_should_be_serviced < self.current_date:
            return True
        else:
            return False
