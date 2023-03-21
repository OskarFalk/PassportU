from __future__ import annotations

class PassportStop:
    _state = None

    def __init__(self, state: State) -> None:
        self.setGame(state)

    def setGame(self, state: State):
        self._state = state
        self._state.game = self

    def presentState(self):
        print(f"You are in the {type(self._state).__name__} area")

    def takeCostumer(self):
        self._state.takeCostumer()

    def askForPass(self):
        self._state.askForPass()

    def approve(self):
        self._state.approve()

    def askCostumerToEnter(self):
        self._state.askCostumerToEnter()
    
    def sendToSearch(self):
        self._state.sendToSearch()

    def deny(self):
        self._state.deny()

    def sendCostumerAway(self):
        self._state.sendCostumerAway()




class State():
    @property
    def game(self) -> PassportStop:
        return self._game
    
    @game.setter
    def game(self, game: PassportStop):
        self._game = game

class Waiting(State):

    def takeCostumer(self) -> None:
        print("Costumer ariving")
        self.game.setGame(Costumer())

    def askForPass(self) -> None:
        print("There is no costumer")

    def approve(self) -> None:
        print("There is no costumer")

    def askCostumerToEnter(self) -> None:
        print("There is no costumer")
    
    def sendToSearch(self) -> None:
        print("There is no costumer")

    def deny(self) -> None:
        print("There is no costumer")

    def sendCostumerAway(self) -> None:
        print("There is no costumer")


class Costumer(State):
    def takeCostumer(self) -> None:
        print("There are already a costumer")

    def askForPass(self) -> None:
        print("Sending Costumer to passport check")
        self.game.setGame(PassportCheck())

    def approve(self) -> None:
        print("Opening Gate")
        self.game.setGame(OpenGate())

    def askCostumerToEnter(self) -> None:
        print("You can not do that")
    
    def sendToSearch(self) -> None:
        print("Sending Costumer to search")
        self.game.setGame(Search())

    def deny(self) -> None:
        print("Costumer has been denied acces")
        self.game.setGame(NotAllowed())

    def sendCostumerAway(self) -> None:
        print("Security came and took the costumer")
        self.game.setGame(Waiting())


class PassportCheck(State):
    def takeCostumer(self) -> None:
        print("There are already a costumer")

    def askForPass(self) -> None:
        print("You are already checking passport")

    def approve(self) -> None:
        print("Opening Gate")
        self.game.setGame(OpenGate())

    def askCostumerToEnter(self) -> None:
        print("You can not do that")
    
    def sendToSearch(self) -> None:
        print("Sending Costumer to passport check")
        self.game.setGame(Search())

    def deny(self) -> None:
        print("Costumer has been denied acces")
        self.game.setGame(NotAllowed())

    def sendCostumerAway(self) -> None:
        print("Security came and took the costumer")
        self.game.setGame(Waiting())


class Search(State):
    def takeCostumer(self) -> None:
        print("There are already a costumer")

    def askForPass(self) -> None:
        print("Sending Costumer to passport check")
        self.game.setGame(PassportCheck())

    def approve(self) -> None:
        print("Opening Gate")
        self.game.setGame(OpenGate())

    def askCostumerToEnter(self) -> None:
        print("You can not do that")
    
    def sendToSearch(self) -> None:
        print("You are already at search")

    def deny(self) -> None:
        print("Costumer has been denied acces")
        self.game.setGame(NotAllowed())

    def sendCostumerAway(self) -> None:
        print("Security came and took the costumer")
        self.game.setGame(Waiting())


class OpenGate(State):
    def takeCostumer(self) -> None:
        print("There are already a costumer")

    def askForPass(self) -> None:
        print("Custumer waiting to be sent in")

    def approve(self) -> None:
        print("Custumer waiting to be sent in")

    def askCostumerToEnter(self) -> None:
        print("The custumer has entered")
        self.game.setGame(Waiting())

    def sendToSearch(self) -> None:
        print("Custumer waiting to be sent in")

    def deny(self) -> None:
        print("Custumer waiting to be sent in")

    def sendCostumerAway(self) -> None:
        print("Security came and took the costumer")
        self.game.setGame(Waiting())


class NotAllowed(State):

    def takeCostumer(self) -> None:
        print("Custumer waiting to be sent away")

    def askForPass(self) -> None:
        print("Custumer waiting to be sent away")

    def approve(self) -> None:
        print("Custumer waiting to be sent away")

    def askCostumerToEnter(self) -> None:
        print("Custumer waiting to be sent away")

    def sendToSearch(self) -> None:
        print("Custumer waiting to be sent away")

    def deny(self) -> None:
        print("Custumer waiting to be sent away")

    def sendCostumerAway(self) -> None:
        print("Security came and took the costumer")
        self.game.setGame(Waiting())




if __name__ == "__main__":
    print("Game Has Started")
    GameState = PassportStop(Waiting())
    GameState.takeCostumer()
    GameState.sendToSearch()
    GameState.sendCostumerAway()



