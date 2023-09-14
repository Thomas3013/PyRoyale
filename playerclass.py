class Player:
    def __init__(self):
        self.__elixir = 0
        self.__leftTower = 3200
        self.__rightTower = 3200
        self.__mainTower = 6000
        self.__playerDeck = []

    # Getter for elixir
    @property
    def elixir(self):
        return self.__elixir

    # Setter for elixir
    @elixir.setter
    def elixir(self, value):
        self.__elixir = value

    # Getter for leftTower
    @property
    def leftTower(self):
        return self.__leftTower

    # Setter for leftTower
    @leftTower.setter
    def leftTower(self, value):
        self.__leftTower = value

    # Getter for rightTower
    @property
    def rightTower(self):
        return self.__rightTower

    # Setter for rightTower
    @rightTower.setter
    def rightTower(self, value):
        self.__rightTower = value

    # Getter for mainTower
    @property
    def mainTower(self):
        return self.__mainTower

    # Setter for mainTower
    @mainTower.setter
    def mainTower(self, value):
        self.__mainTower = value

    # Getter for playerDeck
    @property
    def playerDeck(self):
        return self.__playerDeck

    # Setter for playerDeck to push back a value
    def push_to_player_deck(self, value):
        self.__playerDeck.append(value)



