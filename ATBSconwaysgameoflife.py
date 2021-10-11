import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells:
nextCells = []
for x in range(WIDTH):
    column = []  # Creates a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")  # Add living cells
        else:
            column.append(" ")  # Add dead cells
    nextCells.append(column)  # nextCells is a list of column lists

while True:  # main program loop
    print("\n\n\n\n\n")  # Separate steps with newlines
    currentCells = copy.deepcopy(nextCells)
    # Print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end=" ")  # Print the # or space
        print()  # Print a new line at the end of the row

# Calculate the next step's cells based on current step's cells:
for x in range(WIDTH):
    for y in range(HEIGHT):
        # Get neigbouring co-ordinates
        # % WIDTH ensures leftCoord is alwats between 0 and WIDTH - 1
        leftCoord = (x - 1) % WIDTH
        rightCoord = (x + 1) % WIDTH
        aboveCoord = (y - 1) % HEIGHT
        belowCoord = (y + 1) % HEIGHT

        # Count number of living neighbors:
        numNeighbors = 0
        if currentCells[leftCoord][rightCoord] == "#":
            numNeighbors += 1  # Top-left neighbour is alive
        if currentCells[x][aboveCoord] == "#":
            numNeighbors += 1  # Top neighbour is alive
        if currentCells[rightCoord][aboveCoord] == "#":
            numNeighbors += 1  # Top-right neighbour is alive
        if currentCells[leftCoord][y] == "#":
            numNeighbors += 1  # Left neighbor is alive
        if currentCells[rightCoord][y] == "#":
            numNeighbors += 1  # Right neighbor is alive
        if currentCells[leftCoord][belowCoord] == "#":
            numNeighbors += 1  # Bottom-left neighbor is alive
        if currentCells[x][belowCoord] == "#":
            numNeighbors += 1  # Bottom neighbour is alive
        if currentCells[rightCoord][belowCoord] == "#":
            numNeighbors += 1  # Bottom-rught neighbor is alive

        # Set Cell based on Conway's Game of Life rules:
        if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
            # Living cells with 2 or 3 neighbours stay alive:
            nextCells[x][y] = "#"
        elif currentCells[x][y] == " " and numNeighbors == 3:
            # Dead cells with 3 neighbours become alive:
            nextCells[x][y] = "#"
        else:
            # Everything else stays dead or dies:
            nextCells[x][y] = " "

time.sleep(1)  # Adds 1 second pause to reduce flickering
