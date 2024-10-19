import random

class WumpusWorld:
    def __init__(self):
        self.size = 4
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.agent_position = (0, 0)
        self.wumpus_position = self.place_wumpus()
        self.gold_position = self.place_gold()
        self.pits = self.place_pits()

    def place_wumpus(self):
        while True:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if pos != (0, 0):
                self.grid[pos[0]][pos[1]] = 'W'
                return pos

    def place_gold(self):
        while True:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if pos != (0, 0) and pos != self.wumpus_position:
                self.grid[pos[0]][pos[1]] = 'G'
                return pos

    def place_pits(self):
        pits = []
        while len(pits) < 3:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if pos not in pits and pos != (0, 0) and pos != self.wumpus_position:
                pits.append(pos)
                self.grid[pos[0]][pos[1]] = 'P'
        return pits

    def move_agent(self, direction):
        x, y = self.agent_position
        if direction == 'up' and x > 0:
            self.agent_position = (x - 1, y)
        elif direction == 'down' and x < self.size - 1:
            self.agent_position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.agent_position = (x, y - 1)
        elif direction == 'right' and y < self.size - 1:
            self.agent_position = (x, y + 1)
        else:
            print("Invalid move!")
            return

        self.check_status()

    def check_status(self):
        if self.agent_position == self.wumpus_position:
            print("You've been eaten by the Wumpus! Game over.")
            exit()
        elif self.agent_position in self.pits:
            print("You've fallen into a pit! Game over.")
            exit()
        elif self.agent_position == self.gold_position:
            print("You've found the gold! You win!")
            exit()
        else:
            print(f"Agent is now at {self.agent_position}.")

    def display_grid(self):
        print("\nCurrent Grid:")
        print("  +---+---+---+---+")
        for i in range(self.size):
            print(f"{i} |", end="")
            for j in range(self.size):
                print(f" {self.grid[i][j]} |", end="")
            print("\n  +---+---+---+---+")
        print()

def main():
    game = WumpusWorld()
    game.display_grid()

    while True:
        move = input("Enter your move (up, down, left, right): ").strip().lower()
        game.move_agent(move)

if __name__ == "__main__":
    main()
