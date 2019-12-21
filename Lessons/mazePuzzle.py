maze = [[1,3,1,1,1,1,1],
        [1,0,1,0,0,0,1],
        [1,0,1,0,1,0,0],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [2,0,0,0,0,0,1],
        [3,0,1,0,1,0,0]]

def maze_runner(maze, directions):
    mazeSize = len(maze)

    startPt = []
    finishPt = []

    
    #find start and finishPT
    for i in range(mazeSize):
        for j in range(mazeSize):
            if maze[i][j] == 2:
                startPt = [i, j]
            if maze[i][j] == 3:
                finishPt.append([i, j])
   

    #go through direction
    for direction in directions:
        foresightLocation = []

        if direction == "N":
            foresightLocation = [(startPt[0] - 1), startPt[1]]
            if (foresightLocation[0]) < 0 or (maze[foresightLocation[0]][foresightLocation[1]]) == 1:
                return "Dead"
            else:
                startPt = foresightLocation
        elif direction == "E":
            foresightLocation = [startPt[0], (startPt[1] + 1)]
            if (foresightLocation[1]) >= mazeSize or (maze[foresightLocation[0]][foresightLocation[1]]) == 1:
                return "Dead"
            else:
                startPt = foresightLocation
        elif direction == "S":
            foresightLocation = [startPt[0] + 1, (startPt[1])]
            if (foresightLocation[0]) >= mazeSize or (maze[foresightLocation[0]][foresightLocation[1]]) == 1:
                return "Dead"
            else:
                startPt = foresightLocation
        elif direction == "W":
            foresightLocation = [startPt[0], (startPt[1] - 1)]
            print(foresightLocation , f" Starting Pt: {startPt}")
            if (foresightLocation[1]) < 0 or (maze[foresightLocation[0]][foresightLocation[1]]) == 1:
                return "Dead"
            else:
                startPt = foresightLocation

    if startPt in finishPt:
        return "Finish"
    else:
        return "Lost"

print(maze_runner(maze, ["S"]))