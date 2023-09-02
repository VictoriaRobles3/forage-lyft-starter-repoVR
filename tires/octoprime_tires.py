from tires.tires import Tires

class OctoprimeTires(Tires):

    def __init__(self, tire_usage1, tire_usage2, tire_usage3, tire_usage4):
        self.tire_usage1 = tire_usage1
        self.tire_usage2 = tire_usage2
        self.tire_usage3 = tire_usage3
        self.tire_usage4 = tire_usage4

    def needs_service(self):
        tire_usage = [self.tire_usage1, self.tire_usage2, self.tire_usage3, self.tire_usage4]
        sum = 0
        for i in tire_usage:
            sum += i
            if i >= 3:
                return True
            else:
                return False
