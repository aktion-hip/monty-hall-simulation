import random

class Stage:
    """The stage of the game, containing three doors."""
    def __init__(self):
        self.doors = [Door() for _ in range(3)]
        self.doors[0].setWinner(True)
        random.shuffle(self.doors)

    def setStrategy(self, strategy):
        self.strategy = strategy

    def runFirst(self, doorNr):
        """Select a door and open another one that is not the selected door and not the winner."""
        firstChoice = self.doors[doorNr]
        doorNrs = [0, 1, 2]
        doorNrs.remove(doorNr)
        # create a copy of the doors to avoid modifying the original list
        doorCopy = self.doors.copy()
        doorCopy.remove(firstChoice) # remove the first choice, i.e. the selected door
        doorCopy.remove(self.calculateOpenDoorNr(doorNr, doorNrs)) # remove the door opened by the quizmaster
        self.finalChoice = self.strategy.process(firstChoice, doorCopy[0])

    def calculateOpenDoorNr(self, doorNr, doorNrs):
        if self.doors[doorNr].isWinner():
            # return first of remaining doors
            return self.doors[doorNrs[0]]
        # return the door that is not the winner
        if self.doors[doorNrs[0]].isWinner():
            return self.doors[doorNrs[1]]
        return self.doors[doorNrs[0]]

    def runFinal(self):
        return 1 if self.finalChoice.isWinner() else 0

class Door:
    """A door class, that can be either a winner or not."""
    def __init__(self):
        self._isWinner = False

    def setWinner(self, isWinner):
        self._isWinner = isWinner

    def isWinner(self):
        return self._isWinner

class Strategy:
    """The strategy class, that can be either to stay or switch."""
    def __init__(self, isStay=False):
        self.isStay = isStay

    def process(self, firstSelectionDoor, otherDoor):
        if self.isStay:
            return firstSelectionDoor
        return otherDoor
    
    def __str__(self):
        return "Stay" if self.isStay else "Switch"
    
class Stats:
    def __init__(self):
        self._statistics = [0,0,0]

    def __str__(self):
        return f"[{self._statistics[0]} | {self._statistics[1]} | {self._statistics[2]}] ({self._statistics[0] + self._statistics[1] + self._statistics[2]})"
    
    def add(self, index):
        self._statistics[index] += 1
        return index

# Simulation function
def run_simulation(strategy, max = 100):
    print(f"Running simulation with strategy: {strategy}, (number of runs: {max})")
    statistics = Stats()
    score = 0
    for _ in range(0, max):
        stage = Stage()
        stage.setStrategy(strategy)
        stage.runFirst(statistics.add(random.randint(0, 2)))
        score += stage.runFinal()
    print(f"Score: {score} / {max} (with Strategy: {strategy})")
    print(f"Statistics: {statistics}")

if __name__ == "__main__":
    strategy = Strategy(False)  # Switch strategy
    run_simulation(strategy, 500)
