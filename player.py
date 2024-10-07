class Player:

    def __init__(self, name: str, color: str, symbole: str) -> None:
        self._name = name
        self._color = color
        self._score = 0
        self._symbole = symbole[0]

    def get(self, attr: str):
        if f"_{attr}" in self.__dict__.keys():
            return self.__dict__[f"_{attr}"]

    def set(self, attr: str, value):
        if f"_{attr}" in self.__dict__.keys():
            self.__dict__[f"_{attr}"] = value
