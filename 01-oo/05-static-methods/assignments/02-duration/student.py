# class Duration:
#     def __init__(self,duration):
#         self.__seconds = duration % 60
#         self.__minutes = (duration // 60) % 60
#         self.__hours = duration // 3600

#     @property
#     def seconds(self):
#         return self.__seconds
    
#     @property
#     def minutes(self):
#         return self.__minutes
    
#     @property
#     def hours(self):
#         return self.__hours

#     @staticmethod
#     def from_seconds(duration):
#         return Duration(duration // 60)
    
#     @staticmethod
#     def from_minutes(minutes):
#         return Duration(minutes * 60, minutes)
    
#     @staticmethod
#     def from_hours(hours):
#         return Duration(hours * 3600, hours)

# duration=Duration.from_seconds(60)
# print(duration.seconds)
# print(duration.minutes)

class Duration:
    def __init__(self,duration):
        self.__duration=duration

    @property
    def seconds(self):
        return self.__duration

    @staticmethod
    def from_seconds(duration):
        return Duration(duration)

    @property
    def minutes(self):
        return self.__duration // 60

    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes*60)

    @property
    def hours(self):
        return self.__duration // 3600

    @staticmethod
    def from_hours(hours):
        return Duration(hours*3600)

duration=Duration.from_hours(1)
print(duration.seconds)
print(duration.minutes)