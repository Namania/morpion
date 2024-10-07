from os import system
from random import randint
from time import sleep
from player import Player
from color import Color

class Game:

    def __init__(self, players: list[Player] | None = None) -> None:
        self._running = True
        self._player_number = 2
        self._turn = randint(0, self._player_number - 1)
        self._players = self.init_players() if players is None else players
        self._grid = [[None for j in range(3)] for i in range(3)]

    def get(self, attr: str):
        if f"_{attr}" in self.__dict__.keys():
            return self.__dict__[f"_{attr}"]
    
    def getCurrentPlayer(self) -> Player:
        return self._players[self._turn]

    def set(self, attr: str, value):
        if f"_{attr}" in self.__dict__.keys():
            self.__dict__[f"_{attr}"] = value
    
    def switch(self) -> None:
        self._turn = self._turn + 1 if self._turn + 1 < self._player_number else 0
    
    def isRunning(self) -> bool:
        return self._running

    def init_players(self) -> list[Player]:

        names = []
        for i in range(self._player_number):
            name = ""
            while name == "":
                system("cls")
                name = input(f"Player{i+1} choose your name: ")
            names.append(name)

        colors = []
        for i in range(self._player_number):
            color = ""
            while color.upper() not in Color().getAll():
                system("cls")
                Color().display()
                color = input(f"\n{names[i]} choose your color: ")
            colors.append(color)

        return [Player(names[i], colors[i], "O" if i == 1 else "X") for i in range(self._player_number)]
    
    def to_display(self, obj: Player | None) -> str:
        if isinstance(obj, Player):
            return f"{Color().get(obj.get('color'))}·{Color().get('default')}"
        return "-"
    
    def display(self) -> None:

        system("cls")
        print("\n  1 2 3")
        for i in range(len(self._grid)):
            print(f"{i+1} {self.to_display(self._grid[i][0])} {self.to_display(self._grid[i][1])} {self.to_display(self._grid[i][2])}")
        print()
    
    def display_score(self) -> None:
        print("\n##########")
        print("# Scores #")
        print("##########")
        for player in self._players:
            print(f"{player.get('name')}: {player.get('score')}")
    
    def place(self, pos: tuple[int]) -> bool:
        if self._grid[pos[0]][pos[1]] is None:
            self._grid[pos[0]][pos[1]] = self._players[self._turn]
            return True
        return False
        ...
    
    def pos(self) -> tuple[int]:
        valid_numbers = ["1", "2", "3"]

        column = ''
        while column not in valid_numbers:
            column = input(f"{self.getCurrentPlayer().get('name')} choose column: ")

        row = ''
        while row not in valid_numbers:
            row = input(f"{self.getCurrentPlayer().get('name')} choose row: ")

        return (int(row) - 1, int(column) - 1)
    
    def hasWinner(self) -> Player | None:

        for i in range(0, len(self._grid)):
            temp = ''
            for j in range(0, len(self._grid[i])):
                temp += "-" if self._grid[i][j] is None else self._grid[i][j].get("symbole")
            if temp == 'OOO':
                return self._players[0]
            elif temp == 'XXX':    
                return self._players[1]

        for i in range(0, len(self._grid)):
            temp = ''
            for j in range(0, len(self._grid[i])):
                temp += "-" if self._grid[j][i] is None else self._grid[j][i].get("symbole")
            if temp == 'OOO':
                return self._players[0]
            elif temp == 'XXX':    
                return self._players[1]

        temp = ''
        for i in range(0, len(self._grid)):
            temp += "-" if self._grid[i][i] is None else self._grid[i][i].get("symbole")
        if temp == 'OOO':
            return self._players[0]
        elif temp == 'XXX':    
            return self._players[1]
            
        temp = ''
        for i in range(0, len(self._grid)):
            temp += "-" if self._grid[i][len(self._grid) - (i + 1)] is None else self._grid[i][len(self._grid) - (i + 1)].get("symbole")
            
        if temp == 'OOO':
            return self._players[0]
        elif temp == 'XXX':    
            return self._players[1]

        return None
    
    def isFinish(self) -> bool:
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                if self._grid[i][j] is None:
                    return False
        return True
    
    def end(self, winner: Player | None = None):
        self.set("running", False)
        self.display()
        print(f"{winner.get('name')} win the game !" if winner is not None else "Draw, nobody wins !")
        sleep(5)
