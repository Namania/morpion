class Color():

    def __init__(self) -> None:
        self.RED = '\33[31m'
        self.GREEN = '\33[32m'
        self.YELLOW = '\33[33m'
        self.BLUE = '\33[34m'
        self.PURPLE = '\33[35m'
        self.DEFAULT = '\33[0m'

    def get(self, attr: str) -> str | None:
        if attr.upper() in self.__dict__.keys():
            return self.__dict__[attr.upper()]
        else:
            return None

    def getAll(self) -> list[str]:
        return self.__dict__.keys()

    def display(self) -> None:
        for color in self.__dict__.keys():
            print('- ' + color.lower())
