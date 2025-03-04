class Game:
    def __init__(self,player1,player2):
        self.__player1=player1
        self.__player2=player2
        self.__active_player=self.__player1
        if self.__player1.token==self.__player2.token:
            raise ValueError("Player can't have the same token.")

    def active_player(self):
        return self.__active_player.name
    
    def switch_active(self):
        if self.__active_player==self.__player1:
            self.__active_player=self.__player2
        else:
            self.__active_player=self.__player1

    def board(self):
        return Board.board()
    
    def players(self):
        return f"Player 1: {self.__player1}\nPlayer 2: {self.__player2}\nActive: {self.active_player()}\n"
    

class Board:
    def __init__(self,x=3,y=3):
        self.rijen=x
        self.kolommen=y

    @property
    def rijen(self):
        return self.__rijen
    
    @rijen.setter
    def rijen(self,x):
        if 0>x<3:
            raise ValueError("Waarde kan niet negatief zijn en moet minstens 3 zijn.")
        self.__rijen=x

    @property
    def kolommen(self):
        return self.__kolommen
    
    @kolommen.setter
    def kolommen(self,y):
        if 0>y<3:
            raise ValueError("Waarde kan niet negatief zijn en moet minstens 3 zijn.")
        self.__rijen=y

    def board(self,x,y):
        padding=3
        board=[[" " for _ in range(x)] for _ in range(y)]
        for i,row in enumerate(board):
            print("|".join([cell.ljust(padding) for cell in row]))
            if i<y-1:
                print("-"*(padding*x+(x-1)))

class Player:
    def __init__(self,name,token):
        self.name=name
        self.token=token

        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name (self,name):
            self.__name=name

        @property
        def token(self):
            return self.__token
        
        @token.setter
        def token(self,token):
            self.token=token

    def __str__(self):
        return f"{self.name}, {self.token}"


mauro=Player("Mauro","X")
flor=Player("Flor","O")
game=Game(mauro,flor)
board=Board()
print(game.players())
board.board(3,3)