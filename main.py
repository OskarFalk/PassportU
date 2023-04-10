from __future__ import annotations
from random import randrange
import pygame
import pygame_gui
pygame.init()
import sys

#VARIABLES SETUP
names = ["Morten", "Ib", "phillip"]
lastnames = ["Mortensen", "Bentsen", "Hansen"]

white = (255, 255, 255)
grey = (155, 155, 155)
black = (0, 0, 0)
green = (0, 255, 0)

#PyGame Setup
clock = pygame.time.Clock()
fps = 60
windowSize = (506, 662)
win = pygame.display.set_mode(windowSize)
pygame.display.set_caption("PassportU")
gui_manager = pygame_gui.UIManager(windowSize)

#IMAGES



#MAINCostumerHandler
points = []
fnames = ["Carelyn", "Kylie", "Bianca", "Caylen", "Coy", "Seth", "Candice", "Leonie", "Lane", "Vivian", "Blake", "Matilda", "Porter", "Lillian", "Viola", "Clark", "Glenn", "Jude", "Dante", "Jax", "Drew", "Anise", "Jeremy", "Lashon", "Bree", "Imogen", "Emerson", "Louisa", "Troy", "Olive", "Heath", "Hope", "Denver", "Karilyn", "Elias", "Oliver", "Javan", "Evony", "Ace", "Joan", "Tanner", "Leo", "Sue", "Harrison", "Bailey", "George", "Malachi", "Jack", "Anneliese", "Preston", "Zane", "Bernice", "Syllable", "Annora", "Irene", "Emeline", "Levi", "Bram", "Sharon", "Dominick", "Kent", "Claude", "Carlen", "Jaidyn", "Neil", "Ashten", "Noah", "Cerise", "Elein", "Sean", "Janetta", "Aaron", "Robin", "Carleen", "Rhett", "Benjamin", "Kathryn", "Michael", "Lilibeth", "Brett", "Fern", "Sullivan", "Shane", "Brock", "Amelia", "Ellen", "Grant", "Coralie", "Jae", "Byron", "Tyson", "Amity", "Juliet", "Juan", "Noel", "Trevor", "Lynn", "Julina", "Reese", "Xavier"]
lnames = ["Petersen", "Villarreal", "Ramsey", "Woodard", "Mora", "Oconnell", "Pittman", "Prince", "Owens", "Atkins", "Lyons", "Hartman", "Glover", "Medina", "Hanson", "Blair", "Summers", "Fowler", "Bridges", "Lane", "Chavez", "Fields", "Phillips", "Cole", "Martinez", "Townsend", "Sawyer", "Moss", "Proctor", "Allen", "Key", "Rios", "Wheeler", "Roach", "Fletcher", "Shelton", "Lawrence", "Hobbs", "Lucas", "Rojas", "Frederick", "Ball", "Myers", "Clark", "Hatfield", "Vazquez", "Yoder", "Shepard", "Frost", "Gaines", "Haas", "Reeves", "Murray", "Dawson", "Cisneros", "Wilcox", "Morrow", "Browning", "Peterson", "Wright", "Mills", "Carlson", "Beasley", "Ritter", "Gibbs", "Liu", "Atkinson", "Stanton", "Vega", "Underwood", "Acosta", "Sellers", "Carr", "Trujillo", "Flowers", "Barton", "Bass", "Mcneil", "Dorsey", "Schroeder", "Washington", "Howell", "Barnett", "Mcguire", "Lee", "Kaiser", "Downs", "Mcgrath", "Shields", "Suarez", "Spears", "Vance", "Benton", "Franco", "Mccoy", "Bishop", "Wood", "Li", "Garrett", "Mckenzie"]
currentCostumer = []
nextTen = []
workingTen = []
blacklist = []
badSearch = []

def GetNewNames():
    nextTen.clear()
    blacklist.clear()
    badSearch.clear()
    for x in range(10):
        workingName = (fnames[randrange(len(fnames))] + " " + lnames[randrange(len(lnames))])
        workingTen.append(workingName)
        nextTen.append(workingName)

    for x in range(2):
        workingNum = randrange(len(workingTen))
        blacklist.append(nextTen[workingNum])
        workingTen.pop(workingNum)

    for x in range(2):
        workingNum = randrange(len(workingTen))
        badSearch.append(nextTen[workingNum])
        workingTen.pop(workingNum)


def waitingScene():
    win.fill(black)


#STATE MACHINE SETUP
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
        print("")
        print("Current Blacklist:")
        print(blacklist[0])
        print(blacklist[1])
        print("")
        print("Current Costumers Name is " + currentCostumer[0])
        self._state.askForPass()

    def approve(self):
        self._state.approve()


    def askCostumerToEnter(self):
        if currentCostumer[0] in badSearch or currentCostumer[0] in blacklist:
            for x in range(10):
                if not len(points) == 0:
                    points.pop(0)
            print("You just let a dangerous person come through...")
        else:
            points.append("")
            print("Good Job")
        print("")
        print("")
        print("")
        print("current points: " + str(len(points)))

        self._state.askCostumerToEnter()
    
    def sendToSearch(self):
        print("")
        if currentCostumer[0] in badSearch:
            print("A Gun was found on the individual")
        else:
            print("Nothing was found on the individual")
        self._state.sendToSearch()

    def deny(self):
        self._state.deny()

    def sendCostumerAway(self):
        if currentCostumer[0] in badSearch or currentCostumer[0] in blacklist:
            points.append("")
            print("That was the right call")
        else:
            if not len(points) == 0:
                points.pop(0)
            print("Wrong Choice")
        print("")
        print("")
        print("")
        print("current points: " + str(len(points)))
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
        print("")
        print("Costumer ariving")
        if len(currentCostumer) == 1:
            currentCostumer.pop(0)

        if len(nextTen) == 0:
            GetNewNames()
        else:
            nextTen.pop(0)
        currentCostumer.append(nextTen[0])
        print(currentCostumer[0])
        print("")


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
        self.game.setGame(PassportCheck())

    def approve(self) -> None:
        print("Opening Gate")
        self.game.setGame(OpenGate())

    def askCostumerToEnter(self) -> None:
        print("You can not do that")
    
    def sendToSearch(self) -> None:
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
        print("!!!")
        print("You are already checking passport")
        print("!!!")

    def approve(self) -> None:
        print("Opening Gate")
        self.game.setGame(OpenGate())

    def askCostumerToEnter(self) -> None:
        print("You can not do that")
    
    def sendToSearch(self) -> None:
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
        print("!!!")
        print("You are already at search")
        print("!!!")

    def deny(self) -> None:
        print("Costumer has been denied acces")
        self.game.setGame(NotAllowed())

    def sendCostumerAway(self) -> None:
        print("Security came and took the costumer")
        self.game.setGame(Waiting())


class OpenGate(State):
    def takeCostumer(self) -> None:
        print("Custumer waiting to be sent in")

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


count = 0
if __name__ == "__main__":

    Image = pygame.image.load('Image.png')
    win.blit(Image, (0,0))

    
    print("Game Has Started")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Hi there, this is your first shift in the passport cheecking industry, I will help you getting started.")
    print("When you recive a costumer, you can check their passport, to see if their name is on the black list,")
    print("or you can search them, to see if they have any illegal objects on them.")
    print("If their name is on the blacklist, or they have an illegal object on them, we trust you to send the costumer away.")
    print("If not, then just let them in. To get your first costumer, press t.")
    print("")
    print("")
    



    GameState = PassportStop(Waiting())
    LastRun = 0

    

    run = True
    
    while run:
        clock.tick(fps)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False
                sys.exit()
            
            keys = pygame.key.get_pressed()

            if count == 0:
                if keys[pygame.K_t]:
                        GameState.takeCostumer()
                        count = 1

                if keys[pygame.K_s]:
                        GameState.sendToSearch()
                        count = 1

                if keys[pygame.K_q]:
                        GameState.sendCostumerAway()
                        count = 1
                        
                if keys[pygame.K_p]:
                        GameState.askForPass()
                        count = 1
                        
                if keys[pygame.K_a]:
                        GameState.approve()
                        count = 1
                        
                if keys[pygame.K_e]:
                        GameState.askCostumerToEnter()
                        count = 1
                        
                if keys[pygame.K_d]:
                        GameState.deny()
                        count = 1

# Take Custumer(t); Send To Search(s); Send Custumer Away(q); Ask For Pass(p); Approve(a); Ask Custumer To Enter(e); Deny(d)

            if pygame.key.get_pressed().count(True) == 0:
                count = 0

            gui_manager.draw_ui(win)
    
            pygame.display.update()





