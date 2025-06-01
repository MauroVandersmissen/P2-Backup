from abc import ABC, abstractmethod
import re

class Exercise(ABC):
    def __init__(self, date, distance, duration):
        if not self.is_valid_date(date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        self.date = date # date in YYYY-MM-DD format
        self.distance = distance # distance in km
        self.duration = duration # duration in minutes

    @property
    @abstractmethod
    def is_valid_date(self):
        pass

    @property
    @abstractmethod
    def calories_factor(self):
        pass

    @property
    def calories(self):
        return int((self.distance / (self.duration / 60)) * self.distance * self.calories_factor)
    
    @staticmethod
    def is_valid_date(date_str):
        return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str))
    
    def __eq__(self, other):
        return self.calories == other.calories
        
    def __lt__(self,other):
        return self.calories < other.calories
        
    def __gt__(self,other):
        return self.calories > other.calories

class Run(Exercise):
    def __init__(self, date, distance, duration, elevation):
        super().__init__(date, distance, duration)
        self.elevation = elevation # elevation in percentage

    @property
    def calories_factor(self):
        return 10 * (1 + self.elevation / 100)

    @property
    def calories(self):
        return super().calories

class Swim(Exercise):
    def __init__(self, date, distance, duration):
        if distance <= 0:
            raise ValueError("Distance must be greater than 0.")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")
        if distance / duration > 0.1278:
            raise ValueError("You just broke the world record for Swim! Either you are a superhuman or the data is incorrect.")

        super().__init__(date, distance, duration)

    @property
    def calories_factor(self):
        return 40

    @property
    def calories(self):
        return super().calories

class Ride(Exercise):
    def __init__(self, date, distance, duration, elevation):
        super().__init__(date, distance, duration)
        self.elevation = elevation # elevation in percentage

    @property
    def calories_factor(self):
        return 2 * (1 + self.elevation / 100)

    @property
    def calories(self):
        return super().calories

class ExerciseLog:
    def __init__(self):
        self.__exercises = []

    def add(self, exercise):
        self.__exercises.append(exercise)

    def create_run(self, date, distance, duration, elevation):
        self.add(Run(date, distance, duration, elevation))

    def create_swim(self, date, distance, duration):
        self.add(Swim(date, distance, duration))

    def create_ride(self, date, distance, duration, elevation):
        self.add(Ride(date, distance, duration, elevation))

    def total_calories_burnt(self):
        return sum(exercise.calories for exercise in self.__exercises)
    
    def filter(self, condition):
        return [exercise for exercise in self.__exercises if condition(exercise)]
    
    def filter_by_date(self, date):
        return self.filter(lambda exercise: exercise.date == date)
    
    def filter_by_distance(self, min_distance):
        return self.filter(lambda exercise: exercise.distance >= min_distance)