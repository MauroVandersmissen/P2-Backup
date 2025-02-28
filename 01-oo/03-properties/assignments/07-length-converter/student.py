class LengthConverter:
    def __init__(self):
        self.__distance_in_meter = 0
        
    @property
    def meter(self):
        return self.__distance_in_meter

    @meter.setter
    def meter(self, value):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        self.__distance_in_meter = value

    @property
    def feet(self):
        return self.__distance_in_meter * 3.28084

    @feet.setter
    def feet(self, value):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        self.__distance_in_meter = value / 3.28084

    @property
    def inches(self):
        return self.__distance_in_meter * 39.3701

    @inches.setter
    def inches(self, value):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        self.__distance_in_meter = value / 39.3701

converter = LengthConverter()
converter.meter = 100
print(converter.feet)
print(converter.inches)
print(converter.meter)
converter.feet = 5
print(converter.inches)