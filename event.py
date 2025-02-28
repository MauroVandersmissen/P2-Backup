from abc import ABC, abstractmethod

class Ticket:
    def __init__ (self,ticket_id,ticketType,ticketPrice):
        self.ticket_id=ticket_id
        self.ticketType=ticketType
        self.ticketPrice=ticketPrice

    @property
    def ticket_id(self):
        return self.__ticket_id
    
    @ticket_id.setter
    def ticket_id(self, ticket_id):
        if not Ticket.isValidID(ticket_id):
            raise ValueError("Invalid Ticket ID")
        self.__ticket_id = ticket_id

    @staticmethod
    def isValidID(ticket_id):
        if len(ticket_id) != 8:
            return False
        
        letters = ticket_id[:4]
        
        if not letters.isalpha or letters.isupper() == False:
            return False
        
        numbers = ticket_id[4:8]
        if not numbers.isdigit():
            return False
        
        return True
        
    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Ticket Type: {self.ticketType}, Ticket Price: {self.ticketPrice}"

class Event(ABC):
    def __init__(self,name,max_capacity):
        self.name=name
        self.max_capacity=max_capacity
        self.__tickets={}

    def add_ticket(self,ticket):
        if len(self.__tickets) >= self.max_capacity and ticket.ticket_id not in self.__tickets:
            raise ValueError("Capacity reached or Ticket ID already exists")
        self.__tickets[ticket.ticket_id] = ticket
        
    def remove_ticket(self,ticket_id):
        if ticket_id not in self.__tickets:
            raise ValueError("Ticket ID does not exist")
        del self.__tickets[ticket_id]
        
    @abstractmethod
    def generate_event_summary():
        pass

    @property
    def tickets(self):
        return len(self.__tickets)

class Concert(Event):
    def __init__(self,name,max_capacity,artists):
        super().__init__(name,max_capacity)
        self.artists=artists

    def generate_event_summary(self):
        summary=f"Name: {self.name}\nTotal tickets: {self.tickets}\nArtists:"
        for artist in self.artists:
            summary+=f"\n   -{artist}"
        return summary

class PrivateEvent(Event):
    def __init__(self,name,artist):
        super().__init__(name,50)
        self.artist=artist

    def generate_event_summary(self):
        return f"Name: {self.name}\nTotal tickets: {self.tickets}\nArtist: {self.artist}"
            

# print(isValidID("VIP12345"))
# ticket=Ticket("VIP12345","VIP",1000.0)
# print(ticket)
# event=Event("Concert",5)
# ticket=Ticket("VIP12345","VIP",1000.0)
# event.add_ticket(ticket)
# print(event.__dict__)
# event.remove_ticket(ticket)
# print(event.__dict__)
# concert=Concert("Concert",1000,["Beyonce","Shakira"])
# ticket=Ticket("VIP12345","VIP",1000.0)
# concert.add_ticket(ticket)
# print(concert.generate_event_summary())
private_event=PrivateEvent("The island","Shakira")
ticket=Ticket("VIP12345","VIP",1000.0)
private_event.add_ticket(ticket)
print(private_event.generate_event_summary())