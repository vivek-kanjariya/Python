class Car:
    def __init__(self, Color, Model, Owner, Prize, PastLoan):
        self.Color = Color
        self.Model = Model
        self.Owner = Owner
        self.Prize = Prize
        self.__PastLoan = PastLoan

    def get_Color(self):
        return self.Color

    def get_Model(self):
        return self.Model

    def get_Owner(self):
        return self.Owner

    def sec_Keys(self):
        return self.Prize

    def get_PastLoan(self):
        return self.__PastLoan

    def set_PastLoan(self, PastLoan):
        self.__PastLoan = PastLoan

    def __add__(self, Other):
        return self.Prize + Other.Prize

    def __str__(self):
        return f"Car Color: {self.Color}\nCar Model: {self.Model}\nCar Owner: {self.Owner}\nCar prize: {self.Prize}"


class ElectricCar(Car):
    def __init__(self, Color, Model, Owner, Prize, PastLoan, Electric_Power):
        super().__init__(Color, Model, Owner, Prize, PastLoan)
        self.Electric_Power = Electric_Power

    def __str__(self):
        return f"Car Color: {self.Color}\nCar Model: {self.Model}\nCar Owner: {self.Owner}\nCar prize: {self.Prize}\nCar power: {self.Electric_Power}"


Maruti = Car("White", "S1", "Vivek", "4,00,000", "2,00,000")
Maruti2 = Car("White", "S1", "Vivek", "4,00,000", "2,00,000")
Tesla = ElectricCar("White", "S1", "Vivek", "4,00,000", "2,00,000", "50kWh")

print(Tesla.get_PastLoan())